# Implemente um jogo de adivinhação em que o usuário deve acertar uma palavra secreta. 
# Utilize tratamento de exceções para garantir que o usuário insira apenas letras do alfabeto.

import random

def jogo_adivinhacao_palavra():
    palavras_secretas = ['python', 'programacao', 'desenvolvedor', 'algoritmo', 'computador']
    palavra_secreta = random.choice(palavras_secretas)
    letras_adivinhadas = ['_' for _ in palavra_secreta]
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação de palavras!")
    print("Tente adivinhar a palavra secreta.")
    print(" ".join(letras_adivinhadas))

    while '_' in letras_adivinhadas:
        try:
            palpite = input("Digite uma letra: ").lower()
            if len(palpite) != 1 or not palpite.isalpha():
                raise ValueError("Por favor, digite apenas uma letra do alfabeto.")

            tentativas += 1

            if palpite in palavra_secreta:
                for index, letra in enumerate(palavra_secreta):
                    if letra == palpite:
                        letras_adivinhadas[index] = palpite
                print("Boa! A letra está na palavra.")
            else:
                print("Que pena! A letra não está na palavra.")

            print(" ".join(letras_adivinhadas))

        except ValueError as ve:
            print(f"Entrada inválida: {ve}")

    print(f"Parabéns! Você adivinhou a palavra '{palavra_secreta}' em {tentativas} tentativas.")

jogo_adivinhacao_palavra()
