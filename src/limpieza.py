import pandas as pd

DEPORTES_VALIDOS = {
    "atletismo": "atletismo",
    "baloncesto": "baloncesto",
    "basketball": "baloncesto",
    "boxeo": "boxeo",
    "ciclismo": "ciclismo",
    "futbol": "futbol",
    "fútbol": "futbol",
    "natacion": "natacion",
    "natación": "natacion",
    "natació": "natacion",
    "rugby": "rugby",
    "tenis": "tenis",
    "tennis": "tenis",
    "voleibol": "voleibol",
    "volleyball": "voleibol",
}

EDAD_MIN = 16
EDAD_MAX = 45

PESO_KG_MIN = 55
PESO_KG_MAX = 105

#HES = horas_entrenamiento_semana
HES_MIN = 3
HES_MAX = 25

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
   df = df.copy()

   #normalizar nombres de columnas
   df.columns = df.columns.str.lower().str.strip()

   #validar columnas requeridas
   requeridas = {"nombre","deporte", "edad", "peso_kg", "altura_cm", "frecuencia_cardiaca_bpm", "horas_entrenamiento_semana", "rendimiento_score", "posicion"}
   faltantes = requeridas - set(df.columns)
   if faltantes:
    raise ValueError(f"Columnas faltantes: {faltantes}")

   #limpiar espacios en valores de texto
   for col in ["nombre", "deporte", "posicion"]:
       df[col] = df[col].str.strip()

   #normalizar nombre de deporte
   df["deporte"] = (
       df["deporte"]
       .str.lower()
       .str.strip()
       .replace(DEPORTES_VALIDOS)
   )

   for col in ["peso_kg", "horas_entrenamiento_semana"]:
       df[col] = (
           df[col]
           .astype(str)
           .str.replace(",",".", regex = False)
           .pipe(pd.to_numeric, errors= "coerce")
       )
   #eliminar duplicados antes de calcular estadísticas.
   df = df.drop_duplicates()

   #eliminar outliers con IQR (acotado al rango válido Peso_Kg)
   q1 = df["peso_kg"].quantile(0.25)
   q3 = df["peso_kg"].quantile(0.75)
   iqr = q3 - q1
   li = max(q1 -1.5*iqr, PESO_KG_MIN)
   ls = min(q3 +1.5*iqr, PESO_KG_MAX)
   df = df[(df["peso_kg"] >= li) & (df["peso_kg"] <= ls)]

   #eliminar outliers con IQR (acotado al rango válido HES)
   q1 = df["horas_entrenamiento_semana"].quantile(0.25)
   q3 = df["horas_entrenamiento_semana"].quantile(0.75)
   iqr = q3 - q1
   li = max(q1 -1.5*iqr, HES_MIN)
   ls = min(q3 +1.5*iqr, HES_MAX)
   df = df[(df["horas_entrenamiento_semana"] >= li) & (df["horas_entrenamiento_semana"] <= ls)]

   #descartar pesos fuera de rango válido antes de calcular promedio
   for col in ["peso_kg"]:
       df[col] = df[col].where(df[col].between(PESO_KG_MIN, PESO_KG_MAX))
   #descartar horas de entrenamiento fuera de rango válido antes de calcular promedio
   for col in ["horas_entrenamiento_semana"]:
       df[col] = df[col].where(df[col].between(HES_MIN, HES_MAX))

   #imputar valores faltantes con la media ya limpia
   for col in ["edad", "peso_kg", "altura_cm", "frecuencia_cardiaca_bpm", "horas_entrenamiento_semana", "rendimiento_score"]:
    df[col] = df[col].fillna(df[col].mean())

   return df
