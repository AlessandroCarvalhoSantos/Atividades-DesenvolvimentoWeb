# Crie um programa que peça ao usuário para digitar uma frase e que, 
# em seguida, mostre a posição inicial de cada palavra contida nessa frase.

frase = input("Digite uma frase: ")

posicoes = []
palavras = frase.split()

posicao_atual = 0
for palavra in palavras:
    posicao = frase.find(palavra, posicao_atual)
    posicoes.append((palavra, posicao))
    posicao_atual = posicao + len(palavra)

for palavra, posicao in posicoes:
    print(f"A palavra '{palavra}' começa na posição {posicao}.")
