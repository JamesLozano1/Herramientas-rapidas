import os

def rename_pdfs_to_uppercase(directory):
    if not os.path.exists(directory):
        print(f"El directorio {directory} no existe.")
        return

    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            new_filename = filename.upper()
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renombrado: {filename} -> {new_filename}")

# Especifica el directorio que contiene los archivos PDF

# Opción 1: Usar barras invertidas dobles
# directory = "C:\\Users\\COMPRAS\\Downloads\\Arriendos Debida Diligencia"

# Opción 2: Usar barras normales
# directory = "C:/Users/COMPRAS/Downloads/Arriendos Debida Diligencia"

# Opción 3: Usar cadenas sin formato (raw strings)
directory = r"C:\Users\COMPRAS\Downloads\Arriendos Debida Diligencia\FORMATO DE VINCULACIÓN"

rename_pdfs_to_uppercase(directory)
