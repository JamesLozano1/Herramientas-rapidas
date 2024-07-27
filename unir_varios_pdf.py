import os
import PyPDF2

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()
    for path in paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def get_pdf_files(directory):
    pdf_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def extract_number_from_filename(filename):
    """ Extract the number from the beginning of the filename """
    base = os.path.basename(filename)
    number = ''
    for char in base:
        if char.isdigit():
            number += char
        else:
            break
    return number

def group_files_by_number(files):
    grouped_files = {}
    for file in files:
        number = extract_number_from_filename(file)
        if number:
            if number not in grouped_files:
                grouped_files[number] = {'folder1': [], 'folder2': []}
            if 'FORMATO DE VINCULACIÓN' in file:
                grouped_files[number]['folder1'].append(file)
            elif 'DEBIDAS DILIGENCIAS' in file:
                grouped_files[number]['folder2'].append(file)
    return grouped_files

def main():
    folder1 = r'C:\Users\COMPRAS\Downloads\Arriendos Debida Diligencia\FORMATO DE VINCULACIÓN'
    folder2 = r'C:\Users\COMPRAS\Downloads\Arriendos Debida Diligencia\DEBIDAS DILIGENCIAS'
    output_folder = r'C:\Users\COMPRAS\Downloads\Arriendos Debida Diligencia\FORMATO ARRENDADOR'

    pdf_list_folder1 = get_pdf_files(folder1)
    pdf_list_folder2 = get_pdf_files(folder2)

    all_pdfs = pdf_list_folder1 + pdf_list_folder2
    grouped_files = group_files_by_number(all_pdfs)

    for number, files in grouped_files.items():
        combined_files = files['folder1'] + files['folder2']
        if combined_files:
            output_pdf_path = os.path.join(output_folder, f"{number}_combined.pdf")
            merge_pdfs(combined_files, output_pdf_path)
            print(f"Archivos combinados guardados en: {output_pdf_path}")

if __name__ == '__main__':
    main()
