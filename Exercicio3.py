# Solicita dois números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Verifica se o segundo número é diferente de zero para evitar divisão por zero
if num2 != 0:
    divisao_inteira = num1 // num2
    resto_divisao = num1 % num2

    # Exibe os resultados
    print(f"Divisão inteira: {divisao_inteira}")
    print(f"Resto da divisão: {resto_divisao}")
else:
    print("Erro: não é possível dividir por zero.")
