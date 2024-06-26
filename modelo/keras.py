import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from scikeras.wrappers import KerasRegressor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Cargar los datos
data = pd.read_csv('C:/Users/nadir/OneDrive/Escritorio/uni/TFG/datasets/siuu.csv', encoding='cp1252')

# Separar las variables predictoras y la variable objetivo
X = data.drop('transfer_logaritmo', axis=1)
y = data['transfer_logaritmo']

# Identificar columnas numéricas y categóricas
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = X.select_dtypes(include=['object']).columns

# Preprocesamiento
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Configurar el modelo de Keras
def build_model():
    model = Sequential([
        Input(shape=(X_train.shape[1],)),  # Asegúrate de configurar shape después de preprocesamiento
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# Crear el pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', KerasRegressor(model=build_model, epochs=100, batch_size=10, verbose=1))
])

# Entrenar el modelo
model.fit(X_train, y_train)

# Evaluación del modelo
metrics = model.score(X_test, y_test)
print(f'Coeficiente de determinación R^2 en el conjunto de prueba: {metrics:.2%}')
