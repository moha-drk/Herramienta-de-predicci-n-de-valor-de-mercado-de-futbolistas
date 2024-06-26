import pandas as pd

# Ruta completa al archivo CSV original
ruta_injuries = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\injuries.csv'

# Cargar los datos desde el archivo CSV
df_injuries = pd.read_csv(ruta_injuries)

# Filtrar los datos para la temporada 22/23
df_injuries_22_23 = df_injuries[df_injuries['season_injured'] == '20/21']

# Sustituir la columna 'season_injured' por una nueva columna 'year'
df_injuries_22_23['year'] = 2021
df_injuries_22_23.drop('season_injured', axis=1, inplace=True)

# Ruta para guardar el nuevo archivo CSV
ruta_guardar_injuries = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\injuries_2021.csv'

# Guardar el dataframe modificado en un nuevo archivo CSV
df_injuries_22_23.to_csv(ruta_guardar_injuries, index=False)

print(f"Los datos de la temporada 22/23 han sido filtrados y modificados, y guardados en {ruta_guardar_injuries}")
