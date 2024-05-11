# Considere uma string que contém todas as letras do alfabeto. Escreva um programa em 
# Python que use a função random.choice para escolher continuamente uma letra até 
# que todas as letras do seu nome tenham sido sorteadas. Ao fim, mostre a quantidade 
# de sorteios que foram realizados até a obtenção de todas as letras de seu nome.

import random

alfabeto = "abcdefghijklmnopqrstuvwxyz"

nome = "alessandro"  

letras_nome = set(nome)

letras_sorteadas = set()

contador_sorteios = 0

while not letras_nome.issubset(letras_sorteadas):
    letra_sorteada = random.choice(alfabeto)
    letras_sorteadas.add(letra_sorteada)
    contador_sorteios += 1

print(f"Quantidade de sorteios realizados até obter todas as letras do nome: {contador_sorteios}")
