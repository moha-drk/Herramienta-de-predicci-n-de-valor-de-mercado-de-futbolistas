
# Proyecto de Transferencia de Jugadores de Fútbol

Este repositorio contiene todos los recursos y códigos desarrollados para mi proyecto de Trabajo de Fin de Grado
sobre predicción de precios de transferencia de jugadores de fútbol. El proyecto está estructurado en varias carpetas que contienen diferentes tipos de archivos y scripts necesarios para replicar los análisis y modelos.

## Estructura del Repositorio

- **Modelo**: Esta carpeta contiene todos los scripts de Python necesarios para crear y entrenar el modelo de predicción.
- **Datasets**: Aquí se encuentran todos los conjuntos de datos utilizados para el entrenamiento del modelo. Incluye datos históricos de transferencias, estadísticas de jugadores, etc.
- **Scraping**: Contiene los scripts usados para recolectar datos de diversas fuentes en línea mediante técnicas de web scraping.
- **Interfaz**: Esta carpeta alberga los scripts necesarios para ejecutar la interfaz de usuario desarrollada con Streamlit, que permite interactuar con el modelo de predicción.
- **combinado_datos**: Incluye scripts que facilitan la integración y limpieza de diferentes conjuntos de datos para prepararlos para el análisis.

## Scraping

Para scrapear datos actualizados deberás hacer uso de los scripts en R

## Instalación

Para ejecutar los scripts y utilizar la interfaz, necesitarás instalar algunas dependencias. Asegúrate de tener Python instalado en tu sistema y luego instala las bibliotecas necesarias usando pip. Aquí está la lista de las principales dependencias:

```bash
pip install pandas numpy scikit-learn xgboost streamlit pickle
```

## Uso

Para utilizar el modelo, navega a la carpeta del proyecto y ejecuta el script principal de la interfaz:

```bash
streamlit run app.py
```

Esto iniciará un servidor local y abrirá automáticamente la interfaz en tu navegador predeterminado.

---

Este texto de README proporciona una visión clara del propósito del repositorio, la estructura de los archivos y las instrucciones para configurar el entorno necesario para ejecutar el proyecto. Es importante mantener este archivo actualizado si se realizan cambios en la estructura del proyecto o en las dependencias.
