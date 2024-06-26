import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

# Cargar los datos
def load_data(filepath):
    return pd.read_csv(filepath, encoding='cp1252')  # Ajusta la codificación si es necesario

data = load_data('C:/Users/nadir/OneDrive/Escritorio/uni/TFG/datasets/final_nominal.csv')

# Separar variables predictoras y objetivo
X = data.drop('transfer_logaritmo', axis=1)
y = data['transfer_logaritmo']

# Identificar columnas numéricas y categóricas
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = X.select_dtypes(include=['object']).columns

# Preprocesamiento
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())  # Escalar características numéricas
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Codificar características categóricas
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Configurar el modelo
xgb_model = XGBRegressor(random_state=42)
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('xgb', xgb_model)
])

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Parámetros para GridSearchCV
param_grid = {
    'xgb__n_estimators': [100, 300, 500],
    'xgb__max_depth': [3, 5, 7],
    'xgb__learning_rate': [0.01, 0.1, 0.2],
    'xgb__subsample': [0.7, 0.9, 1.0],
    'xgb__colsample_bytree': [0.7, 0.9, 1.0]
}

# Configurar la búsqueda en cuadrícula
grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='r2', verbose=1)
grid_search.fit(X_train, y_train)

# Mejor modelo y puntuación
best_model = grid_search.best_estimator_
print("Mejor puntuación R^2:", grid_search.best_score_)
print("Mejores parámetros:", grid_search.best_params_)

# Evaluación del modelo en el conjunto de prueba
predictions = best_model.predict(X_test)
r2 = r2_score(y_test, predictions)
print(f'Coeficiente de determinación R^2 en el conjunto de prueba: {r2:.2f}')
