import pandas as pd

# Cargar los datasets
ruta_combined_transfers_balances = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\combined_transfers_balances_2023.csv'
ruta_summary_injuries = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\summary_injuries_2023.csv'

combined_transfers_balances = pd.read_csv(ruta_combined_transfers_balances)
summary_injuries = pd.read_csv(ruta_summary_injuries)

# Realizar un merge left, asumiendo que summary_injuries contiene las columnas 'player_name' y 'total_games_missed'
combined_data = pd.merge(combined_transfers_balances, summary_injuries, on='player_name', how='left')

# Si 'total_games_missed' es NaN (jugador no presente en el dataset de lesiones), reemplazar por 0
combined_data['total_games_missed'] = combined_data['total_games_missed'].fillna(0)

# Guardar el dataframe combinado en un nuevo archivo CSV
ruta_guardar_combinado = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\final_combined_2023.csv'
combined_data.to_csv(ruta_guardar_combinado, index=False)

print(f"El dataset combinado ha sido guardado correctamente en '{ruta_guardar_combinado}'.")
