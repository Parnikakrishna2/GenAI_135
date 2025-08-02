import gradio as gr
from utils import generate_prescription_text, generate_pdf

def full_pipeline(disease, age):
    text = generate_prescription_text(disease, age)
    pdf_path = generate_pdf(disease, age, text)
    return text, pdf_path

with gr.Blocks() as app:
    gr.Markdown("## 🩺 AI Prescription Verifier - Disease to Drug Suggestion")

    disease_input = gr.Textbox(label="Enter Disease")
    age_input = gr.Number(label="Enter Age")

    generate_btn = gr.Button("Generate Prescription")

    output_text = gr.Textbox(label="Prescription")
    output_pdf = gr.File(label="Download PDF")

    generate_btn.click(fn=full_pipeline, inputs=[disease_input, age_input], outputs=[output_text, output_pdf])

app.launch()
