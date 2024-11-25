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
def draw_cat_plot():

    # 5: Crear el DataFrame para el gráfico categórico
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
        var_name='variable', 
        value_name='value'
    )

    # 6: Agrupar y contar los datos
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    
    # 7: Dibujar el gráfico categórico
    fig = sns.catplot(
        x='variable',
        y='size',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar',
        height=5,
        aspect=1.2
    ).fig


    # 8: Guardar el gráfico como archivo
    fig.savefig('catplot.png')
    return fig


# 10: Definir la función para crear el mapa de calor
def draw_heat_map():

    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12: Calcular la matriz de correlación
    corr = df_heat.corr()

    # 13: Generar mask para el triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        cmap='coolwarm',
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5}
    )

    # 15
    fig.savefig('heatmap.png')
    return fig
