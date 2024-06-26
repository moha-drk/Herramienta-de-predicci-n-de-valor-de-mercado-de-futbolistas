import pandas as pd
import os
import unidecode

def normalize_name(name):
    name = unidecode.unidecode(name).lower()
    parts = name.split()
    if len(parts) > 1:
        return f"{parts[0][0]}. {' '.join(parts[1:])}"
    return name

# Rutas de los archivos
transfers_merged_file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\transfers_2022_merged.csv'
injuries_file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\summary_injuries_2021.csv'

# Verificar si los archivos existen
if not os.path.exists(transfers_merged_file_path) or not os.path.exists(injuries_file_path):
    print("Uno o más archivos no existen.")
else:
    # Leer los archivos CSV
    transfers_merged_df = pd.read_csv(transfers_merged_file_path)
    injuries_df = pd.read_csv(injuries_file_path)

    # Normalizar los nombres en transfers_merged y injuries
    transfers_merged_df['normalized_name'] = transfers_merged_df['player_name'].apply(normalize_name)
    injuries_df['normalized_name'] = injuries_df['player_name'].apply(normalize_name)

    # Seleccionar columnas necesarias de injuries
    injuries_columns = ['normalized_name', 'total_games_missed']
    injuries_df = injuries_df[injuries_columns]

    # Realizar el left join entre transfers_merged y injuries
    final_df = pd.merge(transfers_merged_df, injuries_df, on='normalized_name', how='left')

    # Eliminar la columna normalizada después del merge si no es necesaria
    final_df.drop(columns=['normalized_name'], inplace=True)

    # Mostrar los resultados
    print(final_df.head())

    # Guardar el resultado en un nuevo archivo CSV
    output_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\transfers_2022_final.csv'
    final_df.to_csv(output_path, index=False)
    print(f"El dataset final combinado se ha guardado en {output_path}.")
