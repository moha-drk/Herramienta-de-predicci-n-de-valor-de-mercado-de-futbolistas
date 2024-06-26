import pandas as pd
import os

# Rutas a los archivos CSV
final_nominal_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\filtered_final_moha_with_quartiles.csv'
bum_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\bum.csv'

# Leer los archivos CSV con encoding 'ISO-8859-1'
try:
    final_nominal_df = pd.read_csv(final_nominal_path, encoding='ISO-8859-1')
    bum_df = pd.read_csv(bum_path, encoding='ISO-8859-1')
except UnicodeDecodeError:
    print("Error al leer los archivos con encoding 'ISO-8859-1'. Intentando con 'latin1'.")
    final_nominal_df = pd.read_csv(final_nominal_path, encoding='latin1')
    bum_df = pd.read_csv(bum_path, encoding='latin1')

# Columnas comunes entre ambos datasets (excluyendo 'Special')
common_columns = [col for col in final_nominal_df.columns if col in bum_df.columns and col != 'Special']

# Seleccionar solo las columnas comunes de ambos datasets
final_nominal_df = final_nominal_df[common_columns]
bum_df = bum_df[common_columns]

# Concatenar los dos datasets
combined_df = pd.concat([final_nominal_df, bum_df], ignore_index=True)

# Guardar el dataset combinado en un nuevo archivo CSV
output_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\combined_datasett.csv'
combined_df.to_csv(output_path, index=False)
print(f"El dataset combinado se ha guardado en {output_path}.")
