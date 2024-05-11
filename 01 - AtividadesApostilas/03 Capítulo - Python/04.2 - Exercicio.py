# Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, 
# verifique quantas palavras terminam com a letra "o" e quantas terminam com a letra "a".

frase = input("Digite uma frase: ")

palavras = frase.split()

conta_o = 0
conta_a = 0

for palavra in palavras:
    if palavra.endswith('o'):
        conta_o += 1
    if palavra.endswith('a'):
        conta_a += 1

# Exibir os resultados
print(f"Número de palavras que terminam com 'o': {conta_o}")
print(f"Número de palavras que terminam com 'a': {conta_a}")
