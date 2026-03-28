# Proyecto de Análisis de Datos de Deportistas

Este proyecto tiene como objetivo limpiar y analizar un dataset de deportistas para obtener insights sobre su rendimiento y características.

## Estructura del Proyecto

- `data/deportistas.csv`: Dataset original con la información de los deportistas.
- `src/limpieza.py`: Script de Python con funciones para la limpieza y preprocesamiento de los datos.
- `src/analisis.py`: Script de Python con funciones para el análisis de los datos.
- `notebooks/analisis.ipynb`: Notebook de Jupyter que orquesta todo el proceso de carga, limpieza, análisis y exportación de resultados.
- `outputs/`: Carpeta donde se guardan los archivos generados.
  - `deportistas_limpios.csv`: El dataset limpio y procesado.
  - `analisis_por_deporte.csv`: Un análisis que muestra el rendimiento promedio por cada deporte.

## Cómo Ejecutar el Proyecto

1.  **Asegúrate de tener las dependencias instaladas**. Puedes instalarlas usando el archivo `requirements.txt` que creamos anteriormente:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Ejecuta el notebook de análisis** ubicado en `notebooks/analisis.ipynb`. Puedes abrirlo con Jupyter Notebook o Jupyter Lab y correr todas las celdas. Esto generará los archivos de salida en la carpeta `outputs`.

## Pasos Realizados

1.  **Limpieza de Datos (`src/limpieza.py`):**
    - Se normalizaron los nombres de las columnas (minúsculas y sin espacios).
    - Se normalizaron los nombres de los deportes a un formato estándar.
    - Se convirtieron las columnas `peso_kg` y `horas_entrenamiento_semana` a formato numérico, manejando comas como separadores decimales.
    - Se eliminaron filas duplicadas.
    - Se detectaron y eliminaron outliers en `peso_kg` y `horas_entrenamiento_semana` usando el método del Rango Intercuartílico (IQR).
    - Se imputaron los valores faltantes en las columnas numéricas utilizando la media.

2.  **Análisis de Datos (`src/analisis.py`):**
    - `Resumen_datos`: Calcula y muestra el total de deportistas, el rendimiento promedio y la edad promedio.
    - `Promedio_por_deporte`: Calcula el rendimiento promedio agrupado por deporte.
    - `Deportistas_destacados`: Filtra y muestra los deportistas que superan un umbral de rendimiento determinado.

3.  **Orquestación (`notebooks/analisis.ipynb`):**
    - Se carga el dataset original.
    - Se realiza una exploración inicial para identificar problemas como valores nulos y duplicados.
    - Se aplica la función de limpieza.
    - Se ejecutan las funciones de análisis para obtener insights.
    - Se exportan el dataset limpio y los resultados del análisis a la carpeta `outputs`.

## Próximos Pasos

Todo el trabajo realizado en este proyecto se basó en los requisitos especificados en la `Guia3`. Si bien se han cumplido los objetivos principales, se reconoce que podrían existir detalles de limpieza adicionales para que el dataset esté completamente pulido. Estas mejoras menores se abordarán en commits posteriores para refinar aún más la calidad de los datos.
