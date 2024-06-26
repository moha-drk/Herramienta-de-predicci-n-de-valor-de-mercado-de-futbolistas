import pandas as pd
import os

# Ruta al archivo shala.csv
file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\shala.csv'

# Verificar si el archivo existe
if not os.path.exists(file_path):
    print(f"El archivo {file_path} no existe.")
else:
    # Leer el archivo CSV con encoding 'ISO-8859-1'
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        print("Error al leer el archivo con encoding 'ISO-8859-1'. Intentando con 'latin1'.")
        df = pd.read_csv(file_path, encoding='latin1')

    # Eliminar las filas donde transfer_fee es 0
    df = df[df['transfer_fee'] != 0]

    # Eliminar filas consecutivas con el mismo player_name
    df = df[df['player_name'] != df['player_name'].shift()]

    # Mostrar los resultados
    print(df.head())

    # Guardar el resultado en un nuevo archivo CSV
    output_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\shala_filtered.csv'
    df.to_csv(output_path, index=False)
    print(f"El dataset filtrado se ha guardado en {output_path}.")
