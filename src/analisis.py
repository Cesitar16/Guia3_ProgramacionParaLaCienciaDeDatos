import pandas as pd

def Resumen_datos(df: pd.DataFrame):
    """
    Calcula el total de deportistas, promedio de rendimiento y edad promedio.
    """
    total_deportistas = len(df)
    promedio_rendimiento = df["rendimiento_score"].mean()
    edad_promedio = df["edad"].mean()
    
    print(f"Total de deportistas: {total_deportistas}")
    print(f"Promedio de rendimiento: {promedio_rendimiento:.2f}")
    print(f"Edad promedio: {edad_promedio:.2f}")
    
    return total_deportistas, promedio_rendimiento, edad_promedio

def Promedio_por_deporte(df: pd.DataFrame):
    """
    Calcula el promedio de rendimiento agrupado por disciplina deportiva.
    """
    # Se agrupa por la columna 'deporte' y se calcula la media del score
    analisis_deporte = df.groupby("deporte")["rendimiento_score"].mean().reset_index()
    return analisis_deporte

def Deportistas_destacados(df: pd.DataFrame, umbral: float = 7.0):
    """
    Filtra deportistas con un rendimiento_score mayor al umbral indicado (por defecto 7.0).
    """
    destacados = df[df["rendimiento_score"] > umbral]
    return destacados