# Crie um programa que gere um número aleatório entre 1 e 10 e peça para o 
# usuário tentar adivinhar o número. Em caso de erro, o programa deve informar se 
# o número digitado pelo usuário é maior ou menor do que o 
# número gerado (use import random no início e random.randint(1, 10) para obter o número aleatório).

import random

numero_aleatorio = random.randint(1, 10)
adivinhacao = None

print("Tente adivinhar o número que estou pensando, entre 1 e 10!")

while adivinhacao != numero_aleatorio:
    adivinhacao = int(input("Digite seu palpite: "))
    if adivinhacao < numero_aleatorio:
        print("O número que você digitou é menor do que o número gerado. Tente novamente.")
    elif adivinhacao > numero_aleatorio:
        print("O número que você digitou é maior do que o número gerado. Tente novamente.")
    else:
        print("Parabéns! Você adivinhou o número corretamente.")

