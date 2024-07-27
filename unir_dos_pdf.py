import PyPDF2
import tkinter as tk
from tkinter import filedialog

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfFileWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

def select_pdfs():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    pdf_files = filedialog.askopenfilenames(
        title="Selecciona los archivos PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    return root.tk.splitlist(pdf_files)

def select_output_path():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    output_path = filedialog.asksaveasfilename(
        title="Guardar archivo combinado como",
        defaultextension=".pdf",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    return output_path

if __name__ == "__main__":
    pdfs_to_merge = select_pdfs()
    if pdfs_to_merge:
        output_pdf_path = select_output_path()
        if output_pdf_path:
            merge_pdfs(pdfs_to_merge, output_pdf_path)
            print(f"Archivos combinados y guardados en: {output_pdf_path}")
        else:
            print("No se seleccionó la ruta de salida.")
    else:
        print("No se seleccionaron archivos PDF.")
