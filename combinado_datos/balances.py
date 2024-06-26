import pandas as pd

# Ruta al archivo de datos
file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\final_moha_with_quartiles.csv'

# Cargar el DataFrame desde el archivo CSV
data = pd.read_csv(file_path)

# Llenar valores faltantes en 'team_buyer' y 'club_seller' con una categoría 'Unknown'
data['team_buyer'].fillna('Unknown', inplace=True)
data['club_seller'].fillna('Unknown', inplace=True)

# Agrupar y sumar 'transfer_fee' por 'club_seller'
sum_transfer_by_seller = data.groupby('club_seller')['transfer_fee'].sum()

# Ajustar 'income_euros_seller' basado en la suma de 'transfer_fee'
data['income_euros_seller'] = data.apply(
    lambda row: sum_transfer_by_seller.get(row['club_seller'], row['income_euros_seller']) if sum_transfer_by_seller.get(row['club_seller'], 0) > row['income_euros_seller'] else row['income_euros_seller'],
    axis=1
)

# Agrupar y sumar 'transfer_fee' por 'team_buyer'
sum_transfer_by_buyer = data.groupby('team_buyer')['transfer_fee'].sum()

# Ajustar 'expenditure_euros_seller' basado en la suma de 'transfer_fee'
data['expenditure_euros_seller'] = data.apply(
    lambda row: sum_transfer_by_buyer.get(row['team_buyer'], row['expenditure_euros_seller']) if sum_transfer_by_buyer.get(row['team_buyer'], 0) > row['expenditure_euros_seller'] else row['expenditure_euros_seller'],
    axis=1
)

# Crear columnas para balance de compradores y vendedores
data['balance_buyer'] = data['income_euros_buyer'] - data['expenditure_euros_buyer']
data['balance_seller'] = data['income_euros_seller'] - data['expenditure_euros_seller']

# Guardar los cambios en el mismo archivo CSV
data.to_csv(file_path, index=False)
print("Los cambios han sido guardados con éxito en:", file_path)
