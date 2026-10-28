"""
Plant Disease Detection GUI Launcher
Run this script to launch either the Desktop GUI, Streamlit Web App, or Gradio Interface.

Usage:
    python run_gui.py              # Opens interactive selection prompt
    python run_gui.py --desktop    # Launches Native Tkinter Desktop Application
    python run_gui.py --web        # Launches Modern Streamlit Web Application
    python run_gui.py --gradio     # Launches Gradio Interface
"""

import sys
import subprocess
import argparse


def launch_desktop():
    print("Launching Native Desktop GUI (Tkinter)...")
    import gui_desktop
    gui_desktop.main()


def launch_streamlit():
    print("Launching Streamlit Web App...")
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])


def launch_gradio():
    print("Launching Gradio Web App...")
    subprocess.run([sys.executable, "gradio_app.py"])


def main():
    parser = argparse.ArgumentParser(description="Plant Disease Detection GUI Launcher")
    parser.add_argument("--desktop", action="store_true", help="Launch Tkinter Desktop Application")
    parser.add_argument("--web", "--streamlit", action="store_true", help="Launch Streamlit Web App")
    parser.add_argument("--gradio", action="store_true", help="Launch Gradio Web App")

    args = parser.parse_args()

    if args.desktop:
        launch_desktop()
    elif args.web:
        launch_streamlit()
    elif args.gradio:
        launch_gradio()
    else:
        print("=" * 60)
        print("🌿 Plant Disease Detection System — GUI Launcher")
        print("=" * 60)
        print("Select your preferred GUI:")
        print("  1) Streamlit Web GUI   (Modern, Browser-based with Camera support)")
        print("  2) Native Desktop GUI  (Tkinter standalone window, no browser needed)")
        print("  3) Gradio Web GUI      (Lightweight, notebook-compatible web UI)")
        print("=" * 60)
        choice = input("Enter choice (1, 2, or 3) [default: 1]: ").strip()

        if choice == "2":
            launch_desktop()
        elif choice == "3":
            launch_gradio()
        else:
            launch_streamlit()


if __name__ == "__main__":
    main()

