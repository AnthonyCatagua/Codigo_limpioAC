import numpy as np

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True  # Caso especial para el número 2 (único primo par)
    if n % 2 == 0:
        return False  # Descarta números pares mayores que 2
    for i in range(3, int(n**0.5) + 1, 2):  # Solo verifica hasta la raíz cuadrada y solo impares
        if n % i == 0:
            return False
    return True

# Generamos un array de números con NumPy para mayor eficiencia
numeros = np.arange(1, 100001)

# Usamos list comprehensions para filtrar los números primos
primos = [n for n in numeros if es_primo(n)]

print(primos)