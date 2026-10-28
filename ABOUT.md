# 🌿 About This Project: Plant Disease Detection

## 1. Introduction
Agricultural crops are constantly threatened by plant diseases caused by fungi, bacteria, viruses, and pests. Early and accurate detection of these diseases is essential to minimize yield loss, protect food security, and reduce unnecessary pesticide use.

This project delivers an end-to-end **AI-powered Plant Disease Detection System** that automatically classifies leaf diseases from photos and provides immediate, practical treatment recommendations to farmers and gardeners.

---

## 2. Key Objectives
- **Accurate Diagnosis:** Identify 38 different plant leaf conditions across 14 agricultural crops with high precision.
- **Easy Accessibility:** Offer multiple user-friendly Graphical User Interfaces (GUIs)—including a modern web application and a standalone offline desktop application.
- **Actionable Insights:** Provide not just a label, but also the pathogen cause, visual symptoms, organic/chemical remedies, and preventative measures.
- **Fast & Lightweight:** Utilize a pre-trained **MobileNetV2** backbone optimized for rapid inference on standard computers and laptops.

---

## 3. How It Works
1. **Input:** The user uploads a leaf photo or takes a live snapshot using their webcam.
2. **Preprocessing:** The image is resized to `160 x 160` pixels and normalized into the range `[-1, 1]`.
3. **Inference:** A fine-tuned **MobileNetV2** neural network computes the probability distribution across 38 leaf conditions.
4. **Output:** The interface displays:
   - Plant species & condition (Healthy or Diseased)
   - Diagnostic confidence percentage
   - Top-5 alternative predictions
   - Tailored treatment and prevention guide

---

## 4. Supported Crops (14 Species)
- **Fruits:** Apple, Blueberry, Cherry, Grape, Orange (Citrus), Peach, Raspberry, Strawberry
- **Vegetables & Field Crops:** Bell Pepper, Potato, Tomato, Squash, Corn (Maize), Soybean

---

## 5. Technology Stack
- **Deep Learning Framework:** TensorFlow & Keras 3
- **Base Neural Network:** MobileNetV2 (Transfer Learning & Fine-Tuning)
- **Web Interface:** Streamlit & Gradio
- **Desktop Interface:** Python Tkinter & ttk
- **Image Processing:** Pillow (PIL) & NumPy
- **Dataset:** PlantVillage Dataset (54,000+ annotated leaf images)

---

## 6. Project Credits
- **Developer:** Rohan Badge ([GitHub Profile](https://github.com/Rohanbadge))
- **Project IDs:** 23104A0027, 23104A0045
