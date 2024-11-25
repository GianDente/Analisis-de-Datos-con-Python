# Calculadora de varianza, desviación media y estándar

Crea una función llamada `calculate()` en `mean_var_std.py` que use Numpy para producir la media, varianza, desviación estándar, max, min, y suma de las filas, columnas y elementos en una matriz de 3x3.

La entrada de la función debe ser una lista que contenga 9 dígitos. La función debe convertir la lista en una matriz numérica de 3x3 y luego devolver un diccionario que contenga la media, varianza, desviación estándar, max, min, y suma a lo largo de ambos ejes y para la matriz aplanada.

El diccionario retornado debería seguir este formato:

```
{
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
}
```

Si una lista que contiene menos de 9 elementos es pasada a la función, debería levantar una excepción de `ValueError` con el mensaje: "La lista debe contener nueve números". Los valores en el diccionario devuelto deben ser listas y no matrices Numpy.

Por ejemplo, `calculate([0,1,2,3,4,5,6,7,8])` debe regresar:

```
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

```

### Desarrollo
Escribe tu código en `mean_var_std.py.` Para el desarrollo, puedes utilizar `main.py` para probar tu código.