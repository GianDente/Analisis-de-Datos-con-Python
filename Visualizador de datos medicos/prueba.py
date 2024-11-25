import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1: Cargar los datos del archivo CSV
df = pd.read_csv('medical_examination.csv')

# 2: Agregar la columna 'overweight'
df['overweight'] = ( (df['weight'] / ((df['height'] / 100) ** 2) ) > 25).astype(int)

# 3: Normalizar las columnas 'cholesterol' y 'gluc'
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4: Definir la función para crear el gráfico categórico


    # 5: Crear el DataFrame para el gráfico categórico
df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],var_name='variable', value_name='value')
df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

print(df_cat)