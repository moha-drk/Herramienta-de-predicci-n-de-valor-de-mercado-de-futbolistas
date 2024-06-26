import pandas as pd

# Cargar el dataset
file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\2k22_beta.csv'
data = pd.read_csv(file_path)

# Dividir la columna 'appearances_2022' en cuartiles
data['appearances_2022_quartiles'] = pd.qcut(data['appearances_2022'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# Verificar las etiquetas y los rangos
print(data['appearances_2022_quartiles'].value_counts())

# Guardar el nuevo dataset en un archivo diferente para preservar el original
new_file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\2k22_betin.csv'
data.to_csv(new_file_path, index=False)

print(f"Nuevo dataset guardado exitosamente en '{new_file_path}'.")
