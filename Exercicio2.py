import math

# Solicita um número real ao usuário
num = float(input("Digite um número real: "))

# Calcula o quadrado, o cubo e a raiz quadrada
quadrado = num ** 2
cubo = num ** 3

# Verifica se o número é não negativo para calcular a raiz quadrada
if num >= 0:
    raiz_quadrada = math.sqrt(num)
else:
    raiz_quadrada = None

# Exibe os resultados
print(f"Quadrado: {quadrado}")
print(f"Cubo: {cubo}")

if raiz_quadrada is not None:
    print(f"Raiz quadrada: {raiz_quadrada}")
else:
    print("Raiz quadrada: não é possível calcular a raiz quadrada de um número negativo.")
