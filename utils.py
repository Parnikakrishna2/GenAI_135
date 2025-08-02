import pandas as pd
from fpdf import FPDF

# Load dataset once
df = pd.read_csv("final.csv")
df['disease'] = df['disease'].str.strip().str.lower()
df['drug'] = df['drug'].str.strip().str.title()

def generate_prescription_text(disease, age):
    disease = disease.lower().strip()
    match = df[df['disease'].str.contains(disease, na=False)]
    if not match.empty:
        drugs = match['drug'].unique()
        drug_list = ", ".join(drugs)
        advice = (
            f"Patient Age: {age}\n"
            f"Disease: {disease.title()}\n"
            f"Recommended Drug(s): {drug_list}\n"
            f"\nAdditional Advice: Drink plenty of fluids and rest."
        )
    else:
        advice = (
            f"Patient Age: {age}\n"
            f"Disease: {disease.title()}\n"
            "No matching drugs found. Please verify the disease name or try another."
        )
    return advice

def generate_pdf(disease, age, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    file_path = "prescription.pdf"
    pdf.output(file_path)
    return file_path
