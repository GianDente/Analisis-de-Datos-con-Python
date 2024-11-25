# Analizador de datos demográficos

En este desafío debes analizar los datos demográficos usando Pandas. Se le da un conjunto de datos demográficos que fueron extraídos de la base de datos del censo de 1994. Aquí hay un ejemplo de cómo se debería ver:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |


Debes usar Pandas para responder a las siguientes preguntas:

1. ¿Cuántas personas de cada raza están representadas en este conjunto de datos? Debe ser una serie Pandas con los nombres de raza como índice. (columna `race`)
2. ¿Cuál es la edad promedio de los hombres?
3. ¿Cuál es el porcentaje de personas que tienen un grado de licenciatura?
4. ¿Qué porcentaje de personas con una educación avanzada (`Bachelors`, `Masters` o `Doctorate`) generan más de 50k?
5. ¿Qué porcentaje de personas sin una educación avanzada generan más de 50k?
6. ¿Cuál es el mínimo número de horas que una persona trabaja por semana?
7. ¿Qué porcentaje de personas que trabajan el mínimo de horas por semana tienen un salario de más de 50k?
8. ¿Qué país tiene el más alto porcentaje de personas que ganan >50k y cual es ese porcentaje?
9. Identifica la ocupación más popular de aquellos que ganan >50k en India.

Utilice el código de inicio en el archivo `demographic_data_analyzer.py`. Actualice el código para que todas las variables establecidas en `None` se establezcan en el cálculo o código apropiado. Redondea todos los decimales a la décima más cercana.

## Desarrollo

Escribe tu código en `demographic_data_analyzer.py`. Para el desarrollo, puedes utilizar `main.py` para probar tu código.