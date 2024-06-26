import pandas as pd
import numpy as np
import pickle
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_absolute_error

# Cargar los datos
data_path = 'C:/Users/nadir/OneDrive/Escritorio/uni/TFG/datasets/siuun.csv'
data = pd.read_csv(data_path)

# Separar los datos en características y objetivo
X = data.drop('transfer_logaritmo', axis=1)  # Reemplazar 'transfer_logaritmo' por el nombre real de la columna si es diferente
y = data['transfer_logaritmo']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo con los mejores parámetros
model = XGBRegressor(
    colsample_bytree=0.9,
    learning_rate=0.01,
    max_depth=5,
    n_estimators=500,
    subsample=0.7,
    random_state=42
)

# Aplicar validación cruzada
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
predictions = model.predict(X_test)

# Calcular métricas
r2 = r2_score(y_test, predictions)
errors = np.abs((y_test - predictions) / y_test)
mean_relative_error = np.mean(errors) * 100

# Guardar el modelo entrenado
model_path = 'C:/Users/nadir/OneDrive/Escritorio/uni/TFG/models/xgb_model4.pkl'
with open(model_path, 'wb') as file:
    pickle.dump(model, file)

# Imprimir resultados
print(f'Coeficiente de determinación R^2: {r2:.2f}')
print(f'Error absoluto medio de la validación cruzada: {-scores.mean():.2f}')
print(f'Error relativo medio: {mean_relative_error:.2f}%')
print('Modelo correctamente guardado')
