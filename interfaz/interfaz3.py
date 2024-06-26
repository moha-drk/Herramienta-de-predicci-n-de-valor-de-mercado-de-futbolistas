import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Función para cargar el modelo guardado
@st.cache_resource
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model('C:/Users/nadir/OneDrive/Escritorio/uni/TFG/models/xgb_model3.pkl')

# Título de la aplicación
st.title('Predicción de Precios de Transferencia de Futbolistas')

# Crear entradas para el usuario
age = st.number_input("Edad del Jugador", min_value=16, max_value=50, value=25)
goals = st.number_input("Número de Goles", min_value=0, value=0)
appearances = st.number_input("Número de Partidos Jugados", min_value=0, value=0)
preferred_foot = st.selectbox("Pierna Hábil", ['Derecha', 'Izquierda'])
salud = st.selectbox("¿Ha sufrido lesiones el futbolista en la última temporada?", ['Sano', 'Lesión Normal', 'Lesión Grave'])
posicion = st.selectbox("¿En qué posición juega el futbolista?", ['Portero', 'Lateral derecho','Lateral izquierdo', 'Defensa central','Mediocentro defensivo', 'Mediocentro','Banda derecha','Banda izquierda','Mediocentro ofensivo','Delantero centro','Segundo punta', 'Extremo derecho', 'Extremo izquierdo'])
habilidad = st.number_input("Clasifica el talento del jugador (Del 1 al 5)", min_value=1, max_value=5, value=1)
partidos_jugados = st.number_input("Cuantos partidos ha jugado en club en el que está", min_value=0, value=25)
contrato = st.number_input("¿Cuando acaba el contrato del jugador con el club actual?", min_value=2023,max_value=2034, value=2025)

nacionalidad = st.selectbox("Nacionalidad", ['Brasil', 'Alemania','Italia', 'Argentina','España', 'Francia','Inglaterra','Uruguay','Paises Bajos','Croacia', 'Portugal', 'Dinamarca','Bélgica','Iran','Japón','Korea del Sur','Senegal','Ghana','Nigeria','Serbia','Marruecos','Polonia','México','Camerún','Colombia','Suecia','Suiza','Dinamarca','Argelia','Gales','Hungría','Otro'])
fisico = st.selectbox("Constitución física del jugador", ['Delgado y menos de 1.70m', 'Delgado y entre 1.70m y 1.85m','Delgado y más de 1.85m','Normal y menos de 1.70m', 'Normal y entre 1.70m y 1.85m','Normal y más de 1.85m','Ancho y menos de 1.70m', 'Ancho y entre 1.70m y 1.85m','Ancho y más de 1.85m'])
media = st.number_input("Media del jugador en el FIFA", min_value=53, max_value=94, value=70)
esfuerzo = st.number_input("Del 1 al 9, ¿Cómo de sacrificado dirías que es el jugador en los partidos?", min_value=1, max_value=9, value=4)
salario = st.selectbox("Salario", ["Bajo","Medio","Alto"])
ventana = st.selectbox("¿En que mercado se piensa hacer le fichaje?", ["Invierno","Verano"])
cesion = st.selectbox("¿Es una cesión?", ["Si","No"])
income_euros_buyer = st.number_input("Ingresos en euros del equipo comprador", min_value=0, value=0)
expenditure_euros_buyer = st.number_input("Gastos en euros del equipo comprador", min_value=0, value=0)
income_euros_seller = st.number_input("Ingresos en euros del equipo vendedor", min_value=0, value=0)
expenditure_euros_seller = st.number_input("Gastos en euros del equipo vendedor", min_value=0, value=0)
liga_comprador = st.selectbox("Liga del equipo comprador",["Serie A", "Ligue 1", "Bundesliga", "LaLiga", "Premier League", "Premier Liga", "Liga Portugal", "Eredivisie", "Major League Soccer","Jupiler Pro League", "Super League 1", "Super League", "Superliga"])
liga_vendedor = st.selectbox("Liga del equipo vendedor", [ "Bundesliga", "Serie A", "Ligue 1", "Liga Brasil", "Premier League", "Championship", "Super Lig", "Eredivisie", "Jupiler Pro League",
"SuperSport HNL", "LaLiga", "Liga Portugal", "Serie B", "Challenger Pro League", "Ligue 2", "Liga Brasil 2","Fortuna Liga", "Liga Profesional", "Premier Liga", "Premier League 2","efbet Liga", "Prva Liga", "Copa de la Liga", "Super League","Liga Brasil 2", "MLS", "Austrian league", "LaLiga2", "Superliga","Super liga Srbije", "2. Bundesliga", "Serie C - B", "Ekstraklasa" ])
avg_age_in_buyer = st.number_input("Promedio de la edad de los jugadores fichados por el equipo comprador", min_value=16,max_value=35, value=24)
avg_age_in_seller = st.number_input("Promedio de la edad de los jugadores fichados por el equipo vendedor", min_value=16, max_value=35, value=24)


def same_league(a,b):
    if a ==b:
        return 1
    else:
        return 0

def balance(ing,gast):
    return ing-gast

def traducir_ventana(ventana):
    if ventana == "Verano":
        return 1
    else:
        return 2

def loan(cesion):
    if cesion == "Si":
        return 1
    else:
        return 2



def convert_llegada(lla):
    return lla -1

def num_fisico(fis):
    if fis== 'Delgado y menos de 1.70m':
        return 1
    elif fis =='Delgado y entre 1.70m y 1.85m':
        return 2
    elif fis =='Delgado y más de 1.85m':
        return 3
    elif fis == 'Normal y menos de 1.70m':
        return 4
    elif fis == 'Normal y entre 1.70m y 1.85m':
        return 5
    elif fis == 'Normal y más de 1.85m':
        return 6
    elif fis == 'Ancho y menos de 1.70m':
        return 7
    elif fis == 'Ancho y entre 1.70m y 1.85m':
        return 8
    elif fis == 'Ancho y más de 1.85m':
        return 9


# Función para categorizar la nacionalidad directamente desde la entrada en español
def categorize_nationality(nationality):
    elite_countries = ["Brasil", "Alemania", "Italia", "Argentina", "España", "Francia", "Inglaterra", "Uruguay", "Portugal", "Bélgica", "Paises Bajos", "Marruecos"]
    competitive_countries = ["Croacia", "Dinamarca", "Iran", "Japón", "Korea del Sur", "Senegal", "Ghana", "Nigeria", "Serbia", "Polonia", "México", "Camerún", "Colombia", "Suecia", "Suiza", "Dinamarca", "Argelia", "Gales", "Hungría"]

    if nationality in elite_countries:
        return 3
    elif nationality in competitive_countries:
        return 2
    else:
        return 1



def asignar_missed(esp):
    if esp == 'Sano':
        return 3
    elif esp == "Lesión normal":
        return 2
    else:
        return 1

def asignar_salario(esp):
    if esp == 'Bajo':
        return 10000
    elif esp == "Medio":
        return 75000
    else:
        return 750000

# Función para convertir la posición del usuario a la posición del modelo
def convert_position(user_position):
    mapping = {
        'Portero': 1,
        'Lateral derecho': 2,
        'Lateral izquierdo': 12,
        'Defensa central': 4,
        'Mediocentro defensivo': 5,
        'Mediocentro': 8,
        'Banda derecha': 13,
        'Banda izquierda': 6,
        'Mediocentro ofensivo': 10,
        'Delantero centro': 9,
        'Extremo derecho': 7,
        'Extremo izquierdo': 3,
        'Segundo punta':11
    }
    return mapping.get(user_position, "Unknown")  # Retorna "Unknown" si la posición no está en el mapa

def convert_league(user_position):
    mapping = {
        "Serie A":1,
        "Ligue 1":2,
        "Bundesliga":10,
        "LaLiga":15,
        "Premier League":9,
        "Premier Liga":14,
        "Liga Portugal":13,
        "Eredivisie":12,
        "Major League Soccer":18,
        "Jupiler Pro League":4,
        "Super League 1":11,
        "Super League":17,
        "Superliga":8
    }
    return mapping.get(user_position, "Unknown")  # Retorna "Unknown" si la posición no está en el mapa

# Función para clasificar las ligas
def clasificar_liga(league_seller):
    ligas_valor_alto = [
        "Bundesliga", "Serie A", "Ligue 1", "Liga Brasil", "Premier League",
        "Championship", "Super Lig", "Eredivisie", "Jupiler Pro League",
        "SuperSport HNL", "LaLiga", "Liga Portugal"
    ]
    ligas_valor_medio = [
        "Serie B", "Challenger Pro League", "Ligue 2", "Liga Brasil 2",
        "Fortuna Liga", "Liga Profesional", "Premier Liga", "Premier League 2",
        "efbet Liga", "Prva Liga", "Copa de la Liga", "Super League",
        "Liga Brasil 2", "MLS", "Austrian league", "LaLiga2", "Superliga",
        "Super liga Srbije", "2. Bundesliga", "Serie C - B", "Ekstraklasa"
    ]

    if league_seller in ligas_valor_alto:
        return 3
    elif league_seller in ligas_valor_medio:
        return 2
    else:
        return 1



def convert_foot(foot):
    return 1 if foot == 'Derecha' else 2



def pro_vend(zbi):
    if zbi <21.5:
        return 2
    elif zbi<25:
        return 3
    else:
        return 1

# Botón para realizar predicciones
if st.button("Predecir Precio de Transferencia"):
    # Preparar los datos de entrada como un DataFrame que coincide con el esperado por tu modelo
    input_data = pd.DataFrame([[
    age, media, asignar_salario(salario), habilidad, convert_llegada(contrato),
    partidos_jugados, expenditure_euros_seller, income_euros_seller,
    avg_age_in_seller, expenditure_euros_buyer, income_euros_buyer,
    avg_age_in_buyer, appearances, goals, pro_vend(avg_age_in_seller),
    num_fisico(fisico), esfuerzo, balance(income_euros_buyer, expenditure_euros_buyer),
    balance(income_euros_seller, expenditure_euros_seller), convert_foot(preferred_foot),
    loan(cesion), traducir_ventana(ventana), convert_position(posicion),
    convert_league(liga_comprador), same_league(liga_comprador, liga_vendedor),
    clasificar_liga(liga_vendedor), categorize_nationality(nacionalidad), asignar_missed(salud)
    ]], columns=[
    'player_age', 'Overall', 'Wage', 'Skill Moves', 'Contract Valid Until', 'in_squad',
    'expenditure_euros_seller', 'income_euros_seller', 'avg_age_in_seller',
    'expenditure_euros_buyer', 'income_euros_buyer', 'avg_age_in_buyer',
    'appearances_2022', 'goals_2022', 'proyecto_vendedor', 'fisico', 'esfuerzo',
    'balance_buyer', 'balance_seller', 'Preferred Foot', 'is_loan', 'window',
    'player_position', 'league_buyer', 'same_league', 'valor_league_seller', 'nacionalidad', 'salud'
    ])

    # Realizar la predicción
    log_prediction = model.predict(input_data)

    # Convertir la predicción logarítmica a euros
    prediction = np.exp(log_prediction)
    st.write(f"Predicción del Precio de Transferencia: {prediction[0]:.2f} euros")


# Para correr la aplicación, guarda este script como app.py y ejecuta 'streamlit run app.py' desde el terminal

