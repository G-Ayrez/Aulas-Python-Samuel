# Solicita um número inteiro ao usuário
num = int(input("Digite um número inteiro: "))

# Exibe a tabuada de multiplicação de 1 a 10
print(f"Tabuada de multiplicação do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
