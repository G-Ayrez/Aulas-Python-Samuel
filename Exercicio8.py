# Lê um número inteiro do usuário
n = int(input("Digite um número inteiro: "))

# Avalia as expressões lógicas
resultado1 = n > 0 and n % 2 == 0
resultado2 = n > 0 or n % 2 == 0
resultado3 = not (n > 0)

# Exibe os resultados
print(f"n > 0 and n % 2 == 0: {resultado1}")
print(f"n > 0 or n % 2 == 0: {resultado2}")
print(f"not (n > 0): {resultado3}")
