import pandas as pd
import os

# Ruta al archivo 2k22_betin_filtered.csv
file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\2k22_betin_filtered.csv'

# Verificar si el archivo existe
if not os.path.exists(file_path):
    print(f"El archivo {file_path} no existe.")
else:
    # Leer el archivo CSV
    df = pd.read_csv(file_path)

    # Extraer el año de la columna 'joined' y renombrar a 'Year_Joined'
    df['Year_Joined'] = pd.to_datetime(df['joined']).dt.year

    # Eliminar filas donde 'transfer_fee' es un valor faltante
    df = df.dropna(subset=['transfer_fee'])

    # Eliminar la columna original 'joined' si ya no es necesaria
    df.drop(columns=['joined'], inplace=True)

    # Mostrar los resultados
    print(df.head())

    # Guardar el resultado en un nuevo archivo CSV
    output_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\2k22_betin_final.csv'
    df.to_csv(output_path, index=False)
    print(f"El dataset final se ha guardado en {output_path}.")
