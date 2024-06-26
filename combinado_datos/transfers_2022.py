import pandas as pd
import os

# Ruta al archivo de transfers
file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\transfers.csv'

# Verificar si el archivo existe
if not os.path.exists(file_path):
    print(f"El archivo {file_path} no existe.")
else:
    # Leer el archivo CSV
    transfers_df = pd.read_csv(file_path)

    # Verificar si la columna 'year' o similar existe en el DataFrame
    if 'Year' not in transfers_df.columns:
        print("El archivo CSV no contiene una columna 'year'.")
    else:
        # Filtrar los fichajes de 2022
        transfers_2022 = transfers_df[transfers_df['Year'] == 2022]

        # Mostrar los resultados
        print(transfers_2022)

        # Guardar el resultado en un nuevo archivo CSV
        output_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\transfers_2022.csv'
        transfers_2022.to_csv(output_path, index=False)
        print(f"Los fichajes de 2022 se han guardado en {output_path}.")
