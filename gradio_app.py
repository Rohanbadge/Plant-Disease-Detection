"""
Gradio Web Interface for Plant Disease Detection
Enhanced version of the notebook interface with agronomic treatment guidance.
"""

import gradio as gr
from PIL import Image
from model_engine import predict_disease
from disease_info import get_disease_info


def predict_leaf(img):
    if img is None:
        return None, "Please upload or capture a leaf photo."

    # Convert to PIL Image if needed
    if not isinstance(img, Image.Image):
        img = Image.fromarray(img)

    result = predict_disease(img, top_k=5)
    top = result["top_prediction"]
    info = top["info"]

    # Format dictionary of probabilities for Gradio Label component
    top_probs = {item["display_name"]: float(item["confidence"]) for item in result["top_k"]}

    # Detailed markdown report
    status_icon = "🌿 **HEALTHY LEAF**" if top["is_healthy"] else "⚠️ **DISEASE DETECTED**"
    
    report_md = f"""
### {status_icon}
**Diagnosis:** {top['plant']} — {top['condition']}  
**Confidence:** {top['confidence_pct']}%

---
#### 💊 Treatment Recommendations
{info['treatment']}

#### 🌱 Preventative Measures
{info['prevention']}

#### 🔬 Symptoms & Pathogen
- **Pathogen / Cause:** {info['cause']}
- **Key Symptoms:** {info['symptoms']}
"""

    return top_probs, report_md


with gr.Blocks(title="🌿 Plant Disease Detector") as demo:
    gr.Markdown("# 🌿 AI Plant Disease Detection System")
    gr.Markdown(
        "Upload a leaf photo or snap one with your camera. "
        "The MobileNetV2 neural network will identify the disease and provide instant agronomic remedies."
    )

    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type="pil", label="Upload Leaf Photo")
            btn_predict = gr.Button("⚡ Analyze Leaf", variant="primary")

        with gr.Column():
            output_label = gr.Label(num_top_classes=5, label="Top Predictions")
            output_report = gr.Markdown("Awaiting leaf upload...")

    btn_predict.click(
        fn=predict_leaf,
        inputs=input_image,
        outputs=[output_label, output_report]
    )
    input_image.change(
        fn=predict_leaf,
        inputs=input_image,
        outputs=[output_label, output_report]
    )


if __name__ == "__main__":
    demo.launch(inbrowser=True)

