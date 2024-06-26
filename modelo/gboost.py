import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Función para cargar datos, ya que este paso es exitoso con cp1252 según tus logs
def load_data(file_path):
    return pd.read_csv(file_path, encoding='cp1252')

# Ruta del archivo CSV
file_path = 'C:/Users/nadir/OneDrive/Escritorio/uni/TFG/datasets/siuu.csv'

# Cargar datos
data = load_data(file_path)

# Variables predictoras y variable objetivo
X = data.drop('transfer_logaritmo', axis=1)
y = data['transfer_logaritmo']

# Identificar columnas numéricas y categóricas
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = X.select_dtypes(include=['object']).columns

# Preprocesamiento para datos numéricos y categóricos
numerical_transformer = SimpleImputer(strategy='mean')
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Componer preprocesador con ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Crear un pipeline con preprocesador y modelo de Gradient Boosting
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=0))])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular y mostrar el coeficiente de determinación R^2
score = r2_score(y_test, y_pred)
print(f'El porcentaje de acierto del modelo mejorado (coeficiente de determinación R^2): {score:.2%}')
