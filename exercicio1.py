# Solicita dois números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Calcula as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica se o segundo número é diferente de zero para evitar divisão por zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = None

# Exibe os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")

if divisao is not None:
    print(f"Divisão: {divisao}")
else:
    print("Divisão: não é possível dividir por zero.")
