# Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, 
# fatie a frase em substrings de 6 caracteres e mostre-as uma por linha.

frase = input("Digite uma frase: ")

tamanho_substring = 6

for i in range(0, len(frase), tamanho_substring):
    substring = frase[i:i + tamanho_substring]
    print(substring)
