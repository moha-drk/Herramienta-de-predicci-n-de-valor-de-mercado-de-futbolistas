import pandas as pd

# Cargar el dataset modificado
final_dataset_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\final_dataset_modified_2023.csv'
final_dataset = pd.read_csv(final_dataset_path)

# Comprobar y asignar el valor de transfer_fee a 0 donde is_loan es True y transfer_fee es NaN
final_dataset.loc[(final_dataset['is_loan'] == True) & (final_dataset['transfer_fee'].isna()), 'transfer_fee'] = 0

# Guardar los cambios de nuevo en el archivo
final_dataset.to_csv(final_dataset_path, index=False)

print(f"El dataset actualizado ha sido guardado correctamente en '{final_dataset_path}'.")
