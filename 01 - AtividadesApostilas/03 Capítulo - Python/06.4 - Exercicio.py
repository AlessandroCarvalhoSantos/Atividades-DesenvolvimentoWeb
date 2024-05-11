# Faça um programa que leia continuamente o número da camisa (chave) e o nome (valor) de jogadores 
# de futebol, armazenando os dados em um dicionário. O programa deve ler até que o usuário digite 
# -1 no número da camisa. Ao fim, o programa deve mostrar os jogadores ordenados pelo número da camisa.

jogadores = {}

while True:
    numero_camisa = int(input("Digite o número da camisa (ou -1 para terminar): "))
    
    if numero_camisa == -1:
        break
    
    nome_jogador = input("Digite o nome do jogador: ")
    
    jogadores[numero_camisa] = nome_jogador

jogadores_ordenados = dict(sorted(jogadores.items()))

print("Jogadores ordenados pelo número da camisa:")
for numero, nome in jogadores_ordenados.items():
    print(f"Camisa {numero}: {nome}")
