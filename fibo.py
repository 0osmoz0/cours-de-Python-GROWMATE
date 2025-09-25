def fibonacci(n):
    # Cas de base : F(0) = 0 et F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Appel récursif
        return fibonacci(n - 1) + fibonacci(n - 2)

# Exemple d'utilisation
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
