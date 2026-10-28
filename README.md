# 🌿 Plant Disease Detection System

An AI-powered computer vision system for real-time identification and diagnosis of 38 plant leaf diseases using transfer learning with **MobileNetV2**.

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rohanbadge/Plant-Disease-Detection.git
   cd Plant-Disease-Detection
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Quick Start (Running the GUI)

You have **three ways** to run the Graphical User Interface:

### 1. Modern Web Application (Streamlit) — *Recommended*
Features interactive image upload, live camera capture, disease symptoms, treatment recommendations, top-5 confidence breakdown, and a searchable agricultural knowledge base.
- **Run command:**
  ```bash
  python -m streamlit run app.py
  ```
- **Or double-click:** `run_web.bat`

---

### 2. Native Desktop Application (Tkinter)
A standalone Windows desktop application that opens in a native window with no web browser required.
- **Run command:**
  ```bash
  python gui_desktop.py
  ```
- **Or double-click:** `run_desktop.bat`

---

### 3. Gradio Interface
A lightweight web interface matching and expanding the notebook's Gradio deployment.
- **Run command:**
  ```bash
  python gradio_app.py
  ```
- **Or double-click:** `run_gradio.bat`

---

### 4. Interactive Launcher
An all-in-one launcher that lets you select your desired GUI mode from the terminal:
```bash
python run_gui.py
```
Or pass specific flags:
```bash
python run_gui.py --web        # Streamlit
python run_gui.py --desktop    # Tkinter
python run_gui.py --gradio     # Gradio
```

---

## 📁 Project Architecture

```
Plant Disease Detection/
├── Plant_Disease_Detection.ipynb                         # Model training & evaluation notebook
├── plant_disease_model.keras                             # Trained Keras 3.x MobileNetV2 model
├── class_names.json                                      # List of 38 plant disease classes
│
├── app.py                     # Streamlit modern web application
├── gui_desktop.py             # Standalone Tkinter desktop GUI
├── gradio_app.py              # Gradio web application
├── run_gui.py                 # Multi-mode GUI launcher script
│
├── model_engine.py            # Singleton model loader and inference engine
├── disease_info.py            # Knowledge base with symptoms, cause, treatments, prevention
│
├── run_web.bat                # 1-click launcher for Streamlit Web GUI
├── run_desktop.bat            # 1-click launcher for Desktop GUI
├── run_gradio.bat             # 1-click launcher for Gradio GUI
│
└── samples/                   # Ready-to-use sample leaf test images
    ├── sample_healthy_leaf.png
    └── sample_spotted_leaf.png
```

---

## 🌾 Supported Crops & Diseases (38 Classes)

The system covers 14 distinct crops and 38 conditions:
- **Apple:** Apple Scab, Black Rot, Cedar Apple Rust, Healthy
- **Blueberry:** Healthy
- **Cherry:** Powdery Mildew, Healthy
- **Corn (Maize):** Cercospora / Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
- **Grape:** Black Rot, Esca (Black Measles), Leaf Blight (Isariopsis Leaf Spot), Healthy
- **Orange / Citrus:** Huanglongbing (Citrus Greening)
- **Peach:** Bacterial Spot, Healthy
- **Bell Pepper:** Bacterial Spot, Healthy
- **Potato:** Early Blight, Late Blight, Healthy
- **Raspberry:** Healthy
- **Soybean:** Healthy
- **Squash:** Powdery Mildew
- **Strawberry:** Leaf Scorch, Healthy
- **Tomato:** Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Two-Spotted Spider Mite, Target Spot, Tomato Yellow Leaf Curl Virus, Tomato Mosaic Virus, Healthy

---

## 🧠 Model Details
- **Backbone Architecture:** MobileNetV2 (Pretrained on ImageNet)
- **Input Resolution:** `160 x 160 x 3` RGB
- **Input Normalization:** Built-in `Rescaling(1/127.5, offset=-1)`
- **Training Strategy:** Two-phase transfer learning (Phase 1: Feature extractor frozen; Phase 2: Top 30 layers fine-tuned with Adam 1e-5 and EarlyStopping).

