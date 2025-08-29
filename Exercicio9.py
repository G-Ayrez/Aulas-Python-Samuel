# Função para converter texto em booleano
def str_para_bool(s):
    return s.strip().lower() == 'true'

# Solicita os valores booleanos ao usuário
valor1 = input("Digite o primeiro valor booleano (True/False): ")
valor2 = input("Digite o segundo valor booleano (True/False): ")

# Converte os valores para booleanos
bool1 = str_para_bool(valor1)
bool2 = str_para_bool(valor2)

# Realiza as operações lógicas
and_result = bool1 and bool2
or_result = bool1 or bool2
not_bool1 = not bool1
not_bool2 = not bool2

# Exibe os resultados
print(f"{bool1} and {bool2} = {and_result}")
print(f"{bool1} or {bool2} = {or_result}")
print(f"not {bool1} = {not_bool1}")
print(f"not {bool2} = {not_bool2}")
