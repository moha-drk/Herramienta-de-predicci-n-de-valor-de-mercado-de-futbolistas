import pandas as pd

# Cargar los datasets
casicasi_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\casicasi.csv'
balances_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\balances_transferencia_2023.csv'

# Cargar casicasi con encoding cp1252 para evitar problemas de codificación
casicasi = pd.read_csv(casicasi_path, encoding='cp1252')

# Cargar balances
balances = pd.read_csv(balances_path)

# Normalizar los nombres de los equipos en ambos datasets para asegurar coincidencias
casicasi['club_2'] = casicasi['club_2'].str.lower()
balances['squad'] = balances['squad'].str.lower()

# Renombrar las columnas de gastos e ingresos en balances para indicar que pertenecen al club vendedor
balances.rename(columns={'expenditure_euros': 'expenditure_euros_club_2',
                         'income_euros': 'income_euros_club_2'}, inplace=True)

# Unir los datos de balances con casicasi basados en 'club_2' y 'squad'
final_dataset = pd.merge(casicasi, balances, left_on='club_2', right_on='squad', how='left')

# Guardar el dataset final
final_dataset_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\final_casicasi_balances_2023.csv'
final_dataset.to_csv(final_dataset_path, index=False)

print(f"El dataset final con los balances de los clubes vendedores ha sido guardado correctamente en '{final_dataset_path}'.")
