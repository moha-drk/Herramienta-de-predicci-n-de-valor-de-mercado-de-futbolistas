import pandas as pd

# Función para normalizar los nombres de jugadores
def normalize_name(name):
    parts = name.split()
    if len(parts) > 1:
        normalized_name = f"{parts[0][0]}. {' '.join(parts[1:])}"
    else:
        normalized_name = name
    return normalized_name.lower()

# Cargar los datasets
stats_totales_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\stats_totales.csv'
final_dataset_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\final_dataset_2023.csv'

stats_totales = pd.read_csv(stats_totales_path)
final_dataset = pd.read_csv(final_dataset_path)

# Filtrar los datos de stats_totales para el año 2023
stats_totales_2023 = stats_totales[stats_totales['Year'] == 2023]

# Aplicar la normalización de nombres
stats_totales_2023['player_name'] = stats_totales_2023['player_name'].apply(normalize_name)
final_dataset['player_name'] = final_dataset['player_name'].apply(normalize_name)

# Unir los datos en final_dataset con stats_totales basados en el 'player_name' y 'player_pos'
updated_final_dataset = pd.merge(final_dataset, stats_totales_2023, left_on=['player_name', 'player_position'], right_on=['player_name', 'player_pos'], how='left', suffixes=('', '_stats'))

# Actualizar las columnas de appearances, goals, minutes_played desde stats_totales
for col in ['appearances', 'goals', 'minutes_played']:
    updated_final_dataset[col] = updated_final_dataset[col].fillna(updated_final_dataset[col + '_stats'])

# Eliminar las columnas duplicadas y no deseadas
columns_to_drop = ['season_buyer', 'Flag', 'player_pos'] + [col for col in updated_final_dataset if col.endswith('_stats')]
updated_final_dataset.drop(columns_to_drop, axis=1, inplace=True)

# Guardar el dataset modificado
final_dataset_modified_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\final_dataset_modified_2023.csv'
updated_final_dataset.to_csv(final_dataset_modified_path, index=False)

print(f"El dataset modificado ha sido guardado correctamente en '{final_dataset_modified_path}'.")
