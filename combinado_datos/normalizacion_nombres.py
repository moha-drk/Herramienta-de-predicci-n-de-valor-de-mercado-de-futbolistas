import pandas as pd
import unidecode

def normalize_name(name):
    normalized_name = unidecode.unidecode(name)  # Elimina acentos y caracteres especiales
    return normalized_name.lower()  # Convierte el nombre a minúsculas

# Cargar los datasets
carlos_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\carlos_lopez.csv'
fifa_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\fifa_2023.csv'

carlos = pd.read_csv(carlos_path)
fifa = pd.read_csv(fifa_path)

# Normalizar los nombres para compararlos
carlos['player_name'] = carlos['player_name'].apply(normalize_name)
fifa['Name'] = fifa['Name'].apply(normalize_name)

# Columnas específicas de FIFA que queremos transferir
columns_to_add = ["Unnamed: 0", "Overall", "Potential", "Club", "Value(£)", "Wage(£)", "Special", "Preferred Foot",
                  "International Reputation", "Weak Foot", "Skill Moves", "Work Rate", "Body Type",
                  "Contract Valid Until", "Height(cm.)", "Weight(lbs.)", "Release Clause(£)", "Kit Number",
                  "Best Overall Rating", "Year_Joined"]

# Asegurarse de que las columnas existan en carlos para verificar si ya están llenas
for col in columns_to_add:
    if col not in carlos.columns:
        carlos[col] = None  # Añadir las columnas si no existen

# Unir fifa a carlos en base a nombres normalizados
# Solo actualizaremos las filas que aún no tienen datos de FIFA
for index, row in carlos.iterrows():
    if pd.isna(row['Overall']):  # Chequea si la columna 'Overall' está vacía
        fifa_row = fifa[fifa['Name'] == row['player_name']]
        if not fifa_row.empty:
            for col in columns_to_add:
                carlos.at[index, col] = fifa_row.iloc[0][col]

# Guardar el dataset actualizado
carlos.to_csv(carlos_path, index=False)
print(f"El dataset actualizado ha sido guardado correctamente en '{carlos_path}'.")
