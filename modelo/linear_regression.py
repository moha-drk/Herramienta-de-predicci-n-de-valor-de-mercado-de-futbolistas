import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Función para intentar cargar el archivo con diferentes codificaciones
def load_data(file_path, encodings=['utf-8', 'cp1252', 'ISO-8859-1', 'latin1']):
    for enc in encodings:
        try:
            data = pd.read_csv(file_path, encoding=enc)
            print(f"Archivo cargado con éxito usando la codificación {enc}")
            return data
        except UnicodeDecodeError:
            print(f"Fallo al cargar el archivo con la codificación {enc}")
    raise ValueError("No se pudo cargar el archivo con ninguna de las codificaciones proporcionadas")

# Ruta del archivo CSV
file_path = 'C:/Users/nadir/OneDrive/Escritorio/uni/TFG/datasets/siuu.csv'

# Cargar datos con manejo de codificación
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

# Crear un pipeline con preprocesador y el modelo
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular y mostrar el coeficiente de determinación R^2
score = r2_score(y_test, y_pred)
print(f'El porcentaje de acierto del modelo (coeficiente de determinación R^2): {score:.2%}')
