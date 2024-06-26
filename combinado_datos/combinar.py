import pandas as pd

# Rutas de los archivos CSV
ruta_transfers = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\transfers_2022_final.csv'
ruta_balances = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\balances_2022.csv'

# Cargar los datasets
transfers = pd.read_csv(ruta_transfers)
balances = pd.read_csv(ruta_balances)

# Normalizar los nombres de equipos en los datasets
transfers['team_name'] = transfers['team_name'].str.lower()
transfers['club_2'] = transfers['club_2'].str.lower()
balances['squad'] = balances['squad'].str.lower()

# Unir balances para el club comprador (team_name)
transfers = pd.merge(transfers, balances, left_on='team_name', right_on='squad', how='left', suffixes=('', '_buyer'))

# Unir balances para el club vendedor (club_2)
transfers = pd.merge(transfers, balances, left_on='club_2', right_on='squad', how='left', suffixes=('', '_seller'))

# Eliminar columnas duplicadas si las hay
columns_to_drop = [col for col in transfers.columns if '_buyer_buyer' in col or '_seller_seller' in col]
transfers.drop(columns=columns_to_drop, inplace=True)

# Renombrar las columnas de balances del club vendedor para diferenciarlas
transfers.rename(columns={col: col.replace('_seller', '_2') for col in transfers.columns if '_seller' in col}, inplace=True)

# Guardar el dataframe combinado en un nuevo archivo CSV
ruta_guardar_transfers = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\combined_transfers_balances_2022.csv'
transfers.to_csv(ruta_guardar_transfers, index=False)

print(f"Los datos de transferencias y balances han sido combinados y guardados correctamente en '{ruta_guardar_transfers}'.")
