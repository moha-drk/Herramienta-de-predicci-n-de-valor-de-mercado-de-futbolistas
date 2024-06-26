import pandas as pd

# Ruta del archivo original
file_path = 'C:/Users/nadir/OneDrive/Escritorio/uni/TFG/datasets/final_moha_with_quartiles.csv'

# Cargar el dataset
df = pd.read_csv(file_path)

# Filtrar las filas donde transfer_fee es igual a 0
filtered_df = df[df['transfer_fee'] != 0]

# Ruta para guardar el nuevo dataset
new_file_path = 'C:/Users/nadir/OneDrive/Escritorio/uni/TFG/datasets/filtered_final_moha_with_quartiles.csv'

# Guardar el nuevo dataset
filtered_df.to_csv(new_file_path, index=False)

print("El nuevo dataset ha sido guardado.")
