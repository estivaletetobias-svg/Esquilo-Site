import pypdf
import os

pdf_path = "/Users/tobiasestivalete/Downloads/Esquilo - Site/public/assets/PROTOCOLO PEPTÍDEOS EXCLUSIVO PARA ANNA 1.pdf"
output_path = ".agent/scratch/full_content.txt"

with open(pdf_path, 'rb') as f:
    reader = pypdf.PdfReader(f)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n\n"

with open(output_path, 'w') as f:
    f.write(full_text)
