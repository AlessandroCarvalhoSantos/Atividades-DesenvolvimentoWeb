# Implemente um jogo de adivinhação em que o usuário deve acertar um número entre 1 e 10. 
# Utilize tratamento de exceções para garantir que o usuário insira apenas números válidos. 

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 10.")

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            if palpite < 1 or palpite > 10:
                raise ValueError("O número deve estar entre 1 e 10.")
            tentativas += 1
            if palpite == numero_secreto:
                acertou = True
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            elif palpite < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
        except ValueError as ve:
            print(f"Entrada inválida: {ve}")

jogo_adivinhacao()
