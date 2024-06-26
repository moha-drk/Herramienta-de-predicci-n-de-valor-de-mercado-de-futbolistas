import pandas as pd

# Ruta al archivo de datos
file_path = r'C:\Users\nadir\OneDrive\Escritorio\uni\TFG\datasets\final_moha_with_quartiles.csv'

# Cargar el DataFrame desde el archivo CSV
data = pd.read_csv(file_path)

# Cambiar el nombre de las columnas
data.rename(columns={
    'Release Clause(Â£)': 'Release Clause',
    'Value(Â£)': 'Value',
    'Wage(Â£)': 'Wage'
}, inplace=True)

# Modificar valores en la columna 'Special' si son menores de 600, cambiarlos a 1829
data['Special'] = data['Special'].apply(lambda x: 1829 if x < 600 else x)

# Guardar los cambios en el mismo archivo (o en uno nuevo si lo prefieres)
data.to_csv(file_path, index=False)  # Cambia 'file_path' si deseas guardar en un nuevo archivo

print("Los cambios han sido guardados con éxito en:", file_path)
