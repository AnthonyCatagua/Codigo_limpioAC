def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):  # Comprobando TODOS los números menores que n
        if n % i == 0:
            return False
    return True

primos = [n for n in range(1, 100001) if es_primo(n)]

print(primos)
