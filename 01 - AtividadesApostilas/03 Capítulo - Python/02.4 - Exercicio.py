# Crie um programa que peça ao usuário para digitar um número de CPF e verifique se ele é válido. 
# Considere que, para um CPF ser válido, ele deve ter exatamente 11 dígitos inteiros 
# (use a função len(cpf) para obter o tamanho e a função cpf.isdigit para saber se é um número inteiro).

cpf = input("Digite um número de CPF (somente números): ")

if len(cpf) == 11 and cpf.isdigit():
    print("O CPF digitado é válido.")
else:
    print("O CPF digitado é inválido.")
