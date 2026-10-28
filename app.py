"""
Streamlit Web Application for Plant Disease Detection
Interactive, modern web UI for diagnosing plant leaf diseases with actionable remedies.
"""

import os
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

from model_engine import predict_disease, get_class_names
from disease_info import DISEASE_INFO, format_class_name, get_disease_info

# Streamlit Page Configuration
st.set_page_config(
    page_title="Plant Disease Detector AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1b5e20;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4a5568;
        margin-bottom: 1.5rem;
    }
    .status-healthy {
        background-color: #e8f5e9;
        border: 2px solid #4caf50;
        color: #2e7d32;
        padding: 10px 18px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-block;
        margin-bottom: 12px;
    }
    .status-diseased {
        background-color: #ffebee;
        border: 2px solid #ef5350;
        color: #c62828;
        padding: 10px 18px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-block;
        margin-bottom: 12px;
    }
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        margin-bottom: 14px;
    }
    .advice-title {
        font-weight: 700;
        color: #2d3748;
        margin-top: 10px;
        margin-bottom: 4px;
        font-size: 0.95rem;
    }
    .advice-text {
        color: #4a5568;
        font-size: 0.92rem;
        line-height: 1.45;
    }
    .stProgress > div > div > div > div {
        background-color: #2e7d32;
    }
</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?w=500&auto=format&fit=crop&q=60", use_container_width=True)
    st.title("🌱 Leaf Diagnostics")
    st.markdown("**Powered by Deep Learning (MobileNetV2)**")
    st.caption("Trained on 38 plant disease classes from PlantVillage.")
    st.divider()

    mode = st.radio(
        "Navigation",
        ["🔍 Leaf Diagnosis", "📸 Live Camera", "📚 Disease Guide", "📊 Model Info"],
        index=0
    )
    st.divider()
    st.markdown("### 🌾 Supported Crops")
    st.markdown("""
    - **Apple** (Scab, Black Rot, Rust, Healthy)
    - **Blueberry** (Healthy)
    - **Cherry** (Powdery Mildew, Healthy)
    - **Corn** (Gray Spot, Common Rust, Blight, Healthy)
    - **Grape** (Black Rot, Esca, Leaf Blight, Healthy)
    - **Orange / Citrus** (Citrus Greening)
    - **Peach** (Bacterial Spot, Healthy)
    - **Bell Pepper** (Bacterial Spot, Healthy)
    - **Potato** (Early Blight, Late Blight, Healthy)
    - **Raspberry & Soybean** (Healthy)
    - **Squash** (Powdery Mildew)
    - **Strawberry** (Leaf Scorch, Healthy)
    - **Tomato** (9 different conditions + Healthy)
    """)


# Header Section
st.markdown('<div class="main-header">🌿 AI Plant Disease Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload or capture an image of a plant leaf to detect diseases and view actionable treatment recommendations.</div>', unsafe_allow_html=True)


def display_diagnosis(image: Image.Image):
    """Renders leaf diagnosis results and advice."""
    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.subheader("📷 Leaf Photo")
        st.image(image, caption="Submitted leaf image", use_container_width=True)

    with col2:
        with st.spinner("Analyzing leaf with MobileNetV2 neural network..."):
            result = predict_disease(image, top_k=5)

        top = result["top_prediction"]
        info = top["info"]
        is_healthy = top["is_healthy"]

        st.subheader("🧪 Diagnosis Results")

        if is_healthy:
            st.markdown(f'<div class="status-healthy">✅ {top["plant"]} — Healthy Leaf ({top["confidence_pct"]}%)</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="status-diseased">⚠️ {top["plant"]} — {top["condition"]} ({top["confidence_pct"]}%)</div>', unsafe_allow_html=True)

        st.progress(float(top["confidence"]))

        tab_treatment, tab_symptoms, tab_top5 = st.tabs(["💊 Treatment & Prevention", "🔬 Symptoms & Cause", "📊 Top-5 Predictions"])

        with tab_treatment:
            st.markdown('<div class="advice-title">🛡️ Treatment Recommendations:</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="advice-text">{info["treatment"]}</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="advice-title">🌱 Preventative Measures:</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="advice-text">{info["prevention"]}</div>', unsafe_allow_html=True)

        with tab_symptoms:
            st.markdown('<div class="advice-title">🦠 Pathogen / Cause:</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="advice-text">{info["cause"]}</div>', unsafe_allow_html=True)

            st.markdown('<div class="advice-title">🔎 Characteristic Symptoms:</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="advice-text">{info["symptoms"]}</div>', unsafe_allow_html=True)

        with tab_top5:
            st.markdown("##### Model Probability Breakdown")
            chart_data = []
            for item in result["top_k"]:
                chart_data.append({
                    "Condition": item["display_name"],
                    "Confidence (%)": item["confidence_pct"]
                })
            df_chart = pd.DataFrame(chart_data).set_index("Condition")
            st.bar_chart(df_chart, color="#2e7d32")


# MODE 1: Single Image File Upload
if mode == "🔍 Leaf Diagnosis":
    uploaded_file = st.file_uploader("Upload leaf photo (JPG, PNG, JPEG, WEBP)", type=["jpg", "jpeg", "png", "webp"])
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            display_diagnosis(image)
        except Exception as e:
            st.error(f"Error loading image: {e}")
    else:
        st.info("👆 Please upload an image of a plant leaf above to begin diagnosis.")
        st.markdown("#### 🧪 Or test with sample images:")
        sample_col1, sample_col2 = st.columns(2)
        
        sample_path_healthy = os.path.join(os.path.dirname(__file__), "samples", "sample_healthy_leaf.png")
        sample_path_spotted = os.path.join(os.path.dirname(__file__), "samples", "sample_spotted_leaf.png")
        
        with sample_col1:
            if os.path.exists(sample_path_healthy):
                st.image(sample_path_healthy, caption="Healthy Leaf Sample", width=160)
                if st.button("🌿 Diagnose Healthy Leaf Sample"):
                    img = Image.open(sample_path_healthy)
                    display_diagnosis(img)

        with sample_col2:
            if os.path.exists(sample_path_spotted):
                st.image(sample_path_spotted, caption="Spotted / Diseased Leaf Sample", width=160)
                if st.button("⚠️ Diagnose Spotted Leaf Sample"):
                    img = Image.open(sample_path_spotted)
                    display_diagnosis(img)


# MODE 2: Live Camera Capture
elif mode == "📸 Live Camera":
    st.subheader("Capture Live Leaf Image via Camera")
    st.caption("Point your laptop or mobile camera at the plant leaf and take a photo.")
    camera_photo = st.camera_input("Take a leaf picture")
    if camera_photo is not None:
        image = Image.open(camera_photo)
        display_diagnosis(image)


# MODE 3: Disease Guide
elif mode == "📚 Disease Guide":
    st.subheader("📚 Plant Disease & Treatment Knowledge Base")
    st.caption("Explore all 38 plant conditions recognized by this AI model.")

    search_query = st.text_input("🔍 Search by crop or disease name (e.g. Tomato, Rust, Mildew, Potato)", "")
    
    plants = sorted(list(set(info["plant"] for info in DISEASE_INFO.values())))
    selected_plant = st.selectbox("Filter by Plant Type:", ["All Plants"] + plants)

    count = 0
    for key, data in DISEASE_INFO.items():
        if selected_plant != "All Plants" and data["plant"] != selected_plant:
            continue
        if search_query.strip():
            q = search_query.lower()
            if q not in data["plant"].lower() and q not in data["condition"].lower() and q not in data["symptoms"].lower():
                continue

        count += 1
        icon = "🌿" if data["is_healthy"] else "⚠️"
        with st.expander(f"{icon} {data['plant']} — {data['condition']}"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"**Status:** {'Healthy' if data['is_healthy'] else 'Diseased'}")
                st.markdown(f"**Cause:** {data['cause']}")
                st.markdown(f"**Symptoms:** {data['symptoms']}")
            with c2:
                st.markdown(f"**Treatment:** {data['treatment']}")
                st.markdown(f"**Prevention:** {data['prevention']}")

    if count == 0:
        st.warning("No conditions matched your search query.")


# MODE 4: Model Info
elif mode == "📊 Model Info":
    st.subheader("📊 About the Deep Learning Model")
    
    st.markdown("""
    ### Architecture Overview
    - **Base Backbone:** `MobileNetV2` (Pre-trained on ImageNet)
    - **Input Resolution:** `160 x 160 x 3` RGB
    - **Data Augmentation:** Random Flip, Rotation (0.1), Zoom (0.1), Contrast (0.1)
    - **Preprocessing:** Normalization via `Rescaling(1/127.5, offset=-1)` into `[-1, 1]`
    - **Classification Head:**
      - `GlobalAveragePooling2D`
      - `Dropout(0.3)`
      - `Dense(38, activation='softmax')`
    
    ### Training Phases
    1. **Phase 1 (Transfer Learning):** MobileNetV2 backbone frozen; only the classification head trained (Adam lr=1e-3).
    2. **Phase 2 (Fine-Tuning):** Top 30 layers of MobileNetV2 un-frozen; fine-tuned with lower learning rate (Adam lr=1e-5) and EarlyStopping.
    3. **Evaluation:** Tested across 38 leaf conditions with sparse categorical crossentropy.
    """)
    
    st.divider()
    class_list = get_class_names()
    st.markdown(f"**Total Registered Classes:** `{len(class_list)}`")
    with st.expander("View Full List of 38 Classes"):
        for i, c in enumerate(class_list, 1):
            st.markdown(f"{i}. `{c}` -> **{format_class_name(c)}**")
