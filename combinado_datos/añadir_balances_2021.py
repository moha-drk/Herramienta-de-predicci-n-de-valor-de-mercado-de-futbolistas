import pandas as pd
import os

# Ruta al archivo balances_transferencia.csv
balances_file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\balances_transferencia.csv'

# Verificar si el archivo existe
if not os.path.exists(balances_file_path):
    print(f"El archivo {balances_file_path} no existe.")
else:
    # Leer el archivo CSV
    balances_df = pd.read_csv(balances_file_path)

    # Filtrar las filas donde Year == 2021
    balances_2021_df = balances_df[balances_df['Year'] == 2022]

    # Seleccionar solo las columnas necesarias
    selected_columns = ['league', 'squad', 'expenditure_euros', 'income_euros', 'avg_age_out', 'avg_age_in']
    balances_2021_df = balances_2021_df[selected_columns]

    # Mostrar los resultados
    print(balances_2021_df.head())

    # Guardar el resultado en un nuevo archivo CSV
    output_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\balances_2022.csv'
    balances_2021_df.to_csv(output_path, index=False)
    print(f"El dataset filtrado se ha guardado en {output_path}.")
py
