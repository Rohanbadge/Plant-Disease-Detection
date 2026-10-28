"""
Native Desktop GUI for Plant Disease Detection
Built using Tkinter & ttk for responsive, standalone desktop execution on Windows.
"""

import os
import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

from model_engine import predict_disease, get_class_names
from disease_info import get_disease_info, format_class_name


class PlantDiseaseApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("🌿 Plant Disease Detector - AI Leaf Diagnosis")
        self.root.geometry("1020x760")
        self.root.minsize(920, 680)

        # Apply Modern Color Scheme
        self.COLOR_BG = "#f4f6f8"
        self.COLOR_CARD = "#ffffff"
        self.COLOR_PRIMARY = "#2e7d32"
        self.COLOR_PRIMARY_HOVER = "#1b5e20"
        self.COLOR_TEXT = "#1f2937"
        self.COLOR_TEXT_MUTED = "#6b7280"
        self.COLOR_BORDER = "#e5e7eb"
        self.COLOR_HEALTHY = "#2e7d32"
        self.COLOR_DISEASED = "#d32f2f"

        self.root.configure(bg=self.COLOR_BG)
        self.setup_styles()

        self.current_image_path = None
        self.current_pil_image = None
        self.photo_preview = None

        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background=self.COLOR_BG)
        style.configure("Card.TFrame", background=self.COLOR_CARD, relief="flat")
        
        style.configure(
            "Primary.TButton",
            font=("Segoe UI", 10, "bold"),
            background=self.COLOR_PRIMARY,
            foreground="#ffffff",
            padding=8,
            borderwidth=0
        )
        style.map(
            "Primary.TButton",
            background=[("active", self.COLOR_PRIMARY_HOVER), ("disabled", "#a5d6a7")]
        )

        style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 10),
            background="#e2e8f0",
            foreground="#334155",
            padding=8,
            borderwidth=0
        )
        style.map(
            "Secondary.TButton",
            background=[("active", "#cbd5e1")]
        )

        style.configure(
            "Green.Horizontal.TProgressbar",
            troughcolor="#e2e8f0",
            background=self.COLOR_PRIMARY,
            thickness=14
        )

    def create_widgets(self):
        # Header banner
        header_frame = tk.Frame(self.root, bg=self.COLOR_PRIMARY, height=75)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        title_lbl = tk.Label(
            header_frame,
            text="🌿 Plant Disease Detection System",
            font=("Segoe UI", 18, "bold"),
            bg=self.COLOR_PRIMARY,
            fg="#ffffff"
        )
        title_lbl.pack(anchor="w", padx=25, pady=(12, 0))

        sub_lbl = tk.Label(
            header_frame,
            text="Deep Learning AI (MobileNetV2) • 38 Recognized Leaf Conditions • Instant Agricultural Advice",
            font=("Segoe UI", 9),
            bg=self.COLOR_PRIMARY,
            fg="#e8f5e9"
        )
        sub_lbl.pack(anchor="w", padx=25, pady=(2, 10))

        # Main split container
        main_container = tk.Frame(self.root, bg=self.COLOR_BG)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)

        # Left Column (Image & Controls)
        left_col = tk.Frame(main_container, bg=self.COLOR_CARD, bd=1, relief=tk.SOLID)
        left_col.configure(highlightbackground=self.COLOR_BORDER, highlightthickness=1)
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10), ipadx=10, ipady=10)
        left_col.config(width=360)

        img_card_title = tk.Label(
            left_col,
            text="📷 Leaf Image Input",
            font=("Segoe UI", 12, "bold"),
            bg=self.COLOR_CARD,
            fg=self.COLOR_TEXT
        )
        img_card_title.pack(anchor="w", padx=15, pady=(10, 8))

        # Canvas for image preview
        self.canvas = tk.Canvas(
            left_col,
            width=280,
            height=280,
            bg="#f8fafc",
            bd=2,
            relief=tk.GROOVE,
            highlightthickness=0
        )
        self.canvas.pack(padx=15, pady=5)
        self.canvas_text = self.canvas.create_text(
            140, 140,
            text="No Image Selected\n\nClick 'Browse Leaf Photo'\nor 'Load Test Sample'",
            justify=tk.CENTER,
            font=("Segoe UI", 10),
            fill=self.COLOR_TEXT_MUTED
        )

        # File name label
        self.lbl_filename = tk.Label(
            left_col,
            text="File: None",
            font=("Segoe UI", 8),
            bg=self.COLOR_CARD,
            fg=self.COLOR_TEXT_MUTED,
            wraplength=280,
            justify=tk.CENTER
        )
        self.lbl_filename.pack(padx=15, pady=4)

        # Button row
        btn_frame = tk.Frame(left_col, bg=self.COLOR_CARD)
        btn_frame.pack(fill=tk.X, padx=15, pady=10)

        self.btn_browse = ttk.Button(
            btn_frame,
            text="📁 Browse Leaf Photo",
            style="Primary.TButton",
            command=self.browse_image
        )
        self.btn_browse.pack(fill=tk.X, pady=(0, 6))

        sample_btn_frame = tk.Frame(btn_frame, bg=self.COLOR_CARD)
        sample_btn_frame.pack(fill=tk.X, pady=(0, 6))

        self.btn_sample_healthy = ttk.Button(
            sample_btn_frame,
            text="🌿 Healthy Sample",
            style="Secondary.TButton",
            command=self.load_healthy_sample
        )
        self.btn_sample_healthy.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 3))

        self.btn_sample_spotted = ttk.Button(
            sample_btn_frame,
            text="⚠️ Diseased Sample",
            style="Secondary.TButton",
            command=self.load_diseased_sample
        )
        self.btn_sample_spotted.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(3, 0))

        self.btn_diagnose = ttk.Button(
            btn_frame,
            text="⚡ Run Diagnosis",
            style="Primary.TButton",
            command=self.run_diagnosis,
            state=tk.DISABLED
        )
        self.btn_diagnose.pack(fill=tk.X, pady=(4, 0))

        # Right Column (Diagnosis, Advice & Probabilities)
        right_col = tk.Frame(main_container, bg=self.COLOR_CARD, bd=1, relief=tk.SOLID)
        right_col.configure(highlightbackground=self.COLOR_BORDER, highlightthickness=1)
        right_col.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0), ipadx=15, ipady=10)

        res_title = tk.Label(
            right_col,
            text="🧪 Diagnosis & Agronomic Analysis",
            font=("Segoe UI", 12, "bold"),
            bg=self.COLOR_CARD,
            fg=self.COLOR_TEXT
        )
        res_title.pack(anchor="w", padx=15, pady=(10, 5))

        # Result Banner
        self.banner_frame = tk.Frame(right_col, bg="#f1f5f9", relief=tk.FLAT)
        self.banner_frame.pack(fill=tk.X, padx=15, pady=8, ipady=8)

        self.lbl_status_badge = tk.Label(
            self.banner_frame,
            text="Awaiting Leaf Input",
            font=("Segoe UI", 11, "bold"),
            bg="#f1f5f9",
            fg=self.COLOR_TEXT_MUTED,
            padx=10
        )
        self.lbl_status_badge.pack(anchor="w")

        self.lbl_condition_name = tk.Label(
            self.banner_frame,
            text="Please upload an image to view diagnostic results.",
            font=("Segoe UI", 14, "bold"),
            bg="#f1f5f9",
            fg=self.COLOR_TEXT,
            padx=10
        )
        self.lbl_condition_name.pack(anchor="w", pady=(2, 4))

        # Confidence Bar
        conf_container = tk.Frame(self.banner_frame, bg="#f1f5f9", padx=10)
        conf_container.pack(fill=tk.X, pady=(2, 2))

        self.lbl_conf_text = tk.Label(
            conf_container,
            text="Confidence: 0.0%",
            font=("Segoe UI", 9, "bold"),
            bg="#f1f5f9",
            fg=self.COLOR_TEXT
        )
        self.lbl_conf_text.pack(side=tk.LEFT)

        self.progress_conf = ttk.Progressbar(
            conf_container,
            orient=tk.HORIZONTAL,
            mode='determinate',
            style="Green.Horizontal.TProgressbar"
        )
        self.progress_conf.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(15, 0))

        # Notebook for Tabs (Treatment, Prevention, Symptoms, Top-5)
        self.notebook = ttk.Notebook(right_col)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=(10, 10))

        # Tab 1: Treatment & Prevention
        tab_advice = tk.Frame(self.notebook, bg=self.COLOR_CARD)
        self.notebook.add(tab_advice, text="  💊 Treatment & Care  ")

        tk.Label(tab_advice, text="🛡️ Recommended Treatment:", font=("Segoe UI", 10, "bold"), bg=self.COLOR_CARD, fg=self.COLOR_TEXT).pack(anchor="w", padx=10, pady=(8, 2))
        self.txt_treatment = tk.Text(tab_advice, height=4, wrap=tk.WORD, font=("Segoe UI", 9), bg="#f8fafc", bd=1, relief=tk.SOLID)
        self.txt_treatment.pack(fill=tk.X, padx=10, pady=(0, 6))

        tk.Label(tab_advice, text="🌱 Preventative Measures:", font=("Segoe UI", 10, "bold"), bg=self.COLOR_CARD, fg=self.COLOR_TEXT).pack(anchor="w", padx=10, pady=(4, 2))
        self.txt_prevention = tk.Text(tab_advice, height=4, wrap=tk.WORD, font=("Segoe UI", 9), bg="#f8fafc", bd=1, relief=tk.SOLID)
        self.txt_prevention.pack(fill=tk.X, padx=10, pady=(0, 6))

        # Tab 2: Symptoms & Pathogen
        tab_symptoms = tk.Frame(self.notebook, bg=self.COLOR_CARD)
        self.notebook.add(tab_symptoms, text="  🔬 Symptoms & Pathogen  ")

        tk.Label(tab_symptoms, text="🦠 Pathogen / Cause:", font=("Segoe UI", 10, "bold"), bg=self.COLOR_CARD, fg=self.COLOR_TEXT).pack(anchor="w", padx=10, pady=(8, 2))
        self.txt_cause = tk.Text(tab_symptoms, height=3, wrap=tk.WORD, font=("Segoe UI", 9), bg="#f8fafc", bd=1, relief=tk.SOLID)
        self.txt_cause.pack(fill=tk.X, padx=10, pady=(0, 6))

        tk.Label(tab_symptoms, text="🔎 Characteristic Symptoms:", font=("Segoe UI", 10, "bold"), bg=self.COLOR_CARD, fg=self.COLOR_TEXT).pack(anchor="w", padx=10, pady=(4, 2))
        self.txt_symptoms = tk.Text(tab_symptoms, height=4, wrap=tk.WORD, font=("Segoe UI", 9), bg="#f8fafc", bd=1, relief=tk.SOLID)
        self.txt_symptoms.pack(fill=tk.X, padx=10, pady=(0, 6))

        # Tab 3: Top 5 Breakdown
        tab_top5 = tk.Frame(self.notebook, bg=self.COLOR_CARD)
        self.notebook.add(tab_top5, text="  📊 Top 5 Predictions  ")

        self.tree_top5 = ttk.Treeview(
            tab_top5,
            columns=("Rank", "Condition", "Confidence", "Status"),
            show="headings",
            height=6
        )
        self.tree_top5.heading("Rank", text="#")
        self.tree_top5.heading("Condition", text="Plant Condition")
        self.tree_top5.heading("Confidence", text="Probability")
        self.tree_top5.heading("Status", text="Health Status")

        self.tree_top5.column("Rank", width=40, anchor=tk.CENTER)
        self.tree_top5.column("Condition", width=260, anchor=tk.W)
        self.tree_top5.column("Confidence", width=100, anchor=tk.CENTER)
        self.tree_top5.column("Status", width=100, anchor=tk.CENTER)

        self.tree_top5.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Status Bar
        self.status_bar = tk.Label(
            self.root,
            text="Ready. Select an image to diagnose.",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Segoe UI", 8),
            bg="#f1f5f9",
            fg=self.COLOR_TEXT_MUTED,
            padx=10,
            pady=3
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def browse_image(self):
        filetypes = [
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp"),
            ("JPEG Files", "*.jpg *.jpeg"),
            ("PNG Files", "*.png"),
            ("All Files", "*.*")
        ]
        filename = filedialog.askopenfilename(title="Select Plant Leaf Image", filetypes=filetypes)
        if filename:
            self.load_image_file(filename)

    def load_healthy_sample(self):
        sample_path = os.path.join(os.path.dirname(__file__), "samples", "sample_healthy_leaf.png")
        if os.path.exists(sample_path):
            self.load_image_file(sample_path)
            self.lbl_filename.config(text="File: sample_healthy_leaf.png (Sample)")
            self.status_bar.config(text="Healthy sample loaded. Click 'Run Diagnosis'.")
        else:
            messagebox.showwarning("Sample Not Found", f"Sample file not found at {sample_path}")

    def load_diseased_sample(self):
        sample_path = os.path.join(os.path.dirname(__file__), "samples", "sample_spotted_leaf.png")
        if os.path.exists(sample_path):
            self.load_image_file(sample_path)
            self.lbl_filename.config(text="File: sample_spotted_leaf.png (Sample)")
            self.status_bar.config(text="Diseased sample loaded. Click 'Run Diagnosis'.")
        else:
            messagebox.showwarning("Sample Not Found", f"Sample file not found at {sample_path}")

    def load_image_file(self, filepath: str):
        try:
            img = Image.open(filepath)
            self.current_pil_image = img
            self.current_image_path = filepath
            self.lbl_filename.config(text=f"File: {os.path.basename(filepath)}")
            self.display_on_canvas(img)
            self.btn_diagnose.config(state=tk.NORMAL)
            self.status_bar.config(text=f"Loaded: {os.path.basename(filepath)}. Click 'Run Diagnosis'.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image:\n{e}")

    def display_on_canvas(self, img: Image.Image):
        # Resize preserving aspect ratio to fit inside 280x280
        img_copy = img.copy()
        img_copy.thumbnail((270, 270), Image.Resampling.LANCZOS)
        
        self.photo_preview = ImageTk.PhotoImage(img_copy)
        self.canvas.delete("all")
        self.canvas.create_image(140, 140, image=self.photo_preview)

    def run_diagnosis(self):
        if self.current_pil_image is None:
            messagebox.showwarning("Warning", "Please select or load an image first.")
            return

        self.btn_diagnose.config(state=tk.DISABLED)
        self.btn_browse.config(state=tk.DISABLED)
        self.status_bar.config(text="Running MobileNetV2 neural inference...")
        self.root.update_idletasks()

        # Run inference in worker thread to prevent UI freezing
        def worker():
            try:
                res = predict_disease(self.current_pil_image, top_k=5)
                self.root.after(0, self.update_results, res)
            except Exception as e:
                self.root.after(0, self.handle_error, str(e))

        threading.Thread(target=worker, daemon=True).start()

    def handle_error(self, error_msg: str):
        self.btn_diagnose.config(state=tk.NORMAL)
        self.btn_browse.config(state=tk.NORMAL)
        self.status_bar.config(text="Inference failed.")
        messagebox.showerror("Diagnosis Error", f"An error occurred during inference:\n{error_msg}")

    def update_results(self, res: dict):
        self.btn_diagnose.config(state=tk.NORMAL)
        self.btn_browse.config(state=tk.NORMAL)

        top = res["top_prediction"]
        info = top["info"]
        is_healthy = top["is_healthy"]

        # Update banner
        if is_healthy:
            self.banner_frame.config(bg="#e8f5e9")
            self.lbl_status_badge.config(
                text="🌿 HEALTHY PLANT LEAF",
                bg="#e8f5e9",
                fg=self.COLOR_HEALTHY
            )
            self.lbl_condition_name.config(
                text=f"{top['plant']} — Healthy",
                bg="#e8f5e9",
                fg="#1b5e20"
            )
        else:
            self.banner_frame.config(bg="#ffebee")
            self.lbl_status_badge.config(
                text="⚠️ DISEASE DETECTED",
                bg="#ffebee",
                fg=self.COLOR_DISEASED
            )
            self.lbl_condition_name.config(
                text=f"{top['plant']} — {top['condition']}",
                bg="#ffebee",
                fg="#b71c1c"
            )

        conf_pct = top["confidence_pct"]
        self.lbl_conf_text.config(text=f"Confidence: {conf_pct}%", bg=self.banner_frame.cget("bg"))
        self.progress_conf["value"] = conf_pct

        # Update text areas
        def set_text(widget, content):
            widget.config(state=tk.NORMAL)
            widget.delete("1.0", tk.END)
            widget.insert(tk.END, content)
            widget.config(state=tk.DISABLED)

        set_text(self.txt_treatment, info["treatment"])
        set_text(self.txt_prevention, info["prevention"])
        set_text(self.txt_cause, info["cause"])
        set_text(self.txt_symptoms, info["symptoms"])

        # Update Top-5 Treeview
        for item in self.tree_top5.get_children():
            self.tree_top5.delete(item)

        for item in res["top_k"]:
            status_text = "Healthy" if item["is_healthy"] else "Diseased"
            self.tree_top5.insert(
                "",
                tk.END,
                values=(
                    f"#{item['rank']}",
                    item["display_name"],
                    f"{item['confidence_pct']}%",
                    status_text
                )
            )

        self.status_bar.config(text=f"Diagnosis complete: {top['display_name']} ({conf_pct}%)")


def main():
    root = tk.Tk()
    app = PlantDiseaseApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
