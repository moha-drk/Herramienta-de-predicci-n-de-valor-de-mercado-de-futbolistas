import pandas as pd

# Ruta al archivo combinado
combined_dataset_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\combined_dataset.csv'

# Leer el dataset combinado
combined_df = pd.read_csv(combined_dataset_path, encoding='ISO-8859-1')

# Eliminar las columnas especificadas
columns_to_drop = [
    'total_games_missed', 'Weak Foot', 'Year_Joined', 'avg_age_out_seller',
    'avg_age_out_buyer', 'minutes_played_2022', 'appearances_2022_quartiles',
    'posicion', 'gasto_league_buyer', 'goles', 'calidad', 'salario',
    'valor_posicion', 'edad', 'proyecto_comprador'
]

filtered_df = combined_df.drop(columns=columns_to_drop)

# Crear las nuevas variables balance_buyer y balance_seller
filtered_df['balance_buyer'] = filtered_df['income_euros_buyer'] - filtered_df['expenditure_euros_buyer']
filtered_df['balance_seller'] = filtered_df['income_euros_seller'] - filtered_df['expenditure_euros_seller']

# Guardar el resultado en un nuevo archivo CSV
output_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\filtered_combined_dataset.csv'
filtered_df.to_csv(output_path, index=False)
print(f"El dataset filtrado y modificado se ha guardado en {output_path}.")
