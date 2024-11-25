import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la lista en una matriz 3x3
    matrix = np.array(list).reshape(3, 3)
    
    # Calcular las estadísticas
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.flatten().mean().tolist()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.flatten().var().tolist()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.flatten().std().tolist()]
    max_value = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.flatten().max().tolist()]
    min_value = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.flatten().min().tolist()]
    sum_value = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.flatten().sum().tolist()]

    # Crear el diccionario con los resultados
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }

    return calculations

# results = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

# for key, value in results.items():
#    print(f"{key}:\n{value}\n")

