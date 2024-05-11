# Crie um programa que peça ao usuário para digitar uma palavra. 
# O programa deve então indicar se a palavra inserida começa com uma vogal ou uma consoante.

palavra = input("Digite uma palavra: ")

if palavra == "":
    print("Você não digitou uma palavra.")
else:
    primeira_letra = palavra[0].lower()
    vogais = {'a', 'e', 'i', 'o', 'u'}
    if primeira_letra in vogais:
        print(f"A palavra '{palavra}' começa com uma vogal.")
    else:
        print(f"A palavra '{palavra}' começa com uma consoante.")
