import pandas as pd

# Ruta del archivo CSV de lesiones
ruta_injuries = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\injuries_2021.csv'

# Cargar el dataset de lesiones
injuries = pd.read_csv(ruta_injuries)

# Asegurar que 'games_missed' es un valor numérico y manejar posibles valores nulos
injuries['games_missed'] = pd.to_numeric(injuries['games_missed'], errors='coerce').fillna(0)

# Agrupar por 'player_name' y sumar los 'games_missed'
summary_injuries = injuries.groupby('player_name')['games_missed'].sum().reset_index()

# Renombrar las columnas para claridad
summary_injuries.columns = ['player_name', 'total_games_missed']

# Guardar el nuevo dataset resumido en un archivo CSV
ruta_guardar_resumen = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\summary_injuries_2021.csv'
summary_injuries.to_csv(ruta_guardar_resumen, index=False)

print(f"El resumen de partidos perdidos por jugador ha sido guardado correctamente en '{ruta_guardar_resumen}'.")
