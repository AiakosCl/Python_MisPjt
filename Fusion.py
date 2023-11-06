import PyPDF2

# Lista de nombres de los archivos PDF que deseas fusionar
pdf_files = ["1.pdf", "2.pdf", "3.pdf"]

# Crea un objeto PdfWriter
pdf_writer = PyPDF2.PdfWriter()

# Itera a través de los archivos PDF y agrega sus páginas al PdfWriter
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

# Nombre del archivo de salida
output_filename = "Evaluacion_BHP.pdf"

# Crea el archivo PDF fusionado
with open(output_filename, "wb") as output_file:
    pdf_writer.write(output_file)

print(f"Se han fusionado los archivos PDF en {output_filename}")
