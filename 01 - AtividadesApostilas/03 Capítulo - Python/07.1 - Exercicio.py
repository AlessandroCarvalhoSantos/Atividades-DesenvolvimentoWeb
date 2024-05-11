# Crie um programa que solicite ao usuário o nome de um arquivo e que renomeie esse arquivo 
# adicionando a palavra "renomeado" ao nome existente, mantendo sua extensão. 

import os

nome_arquivo = input("Digite o nome do arquivo (com extensão): ")

if os.path.isfile("files/"+nome_arquivo):
    nome, extensao = os.path.splitext("files/"+nome_arquivo)

    novo_nome_arquivo = f"{nome}_renomeado{extensao}"
    os.rename("files/"+nome_arquivo, novo_nome_arquivo)

    print(f"O arquivo foi renomeado para: {novo_nome_arquivo}")
else:
    print("Arquivo não encontrado.")
