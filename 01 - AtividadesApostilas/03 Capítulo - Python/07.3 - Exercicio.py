# Crie um programa que solicite ao usuário o nome de arquivo existente na mesma 
# pasta, copie-o para um novo arquivo mudando a extensão para ".cópia" e exiba o resultado da operação 
# na tela. 


import os
import shutil

nome_arquivo = input("Digite o nome do arquivo (com extensão): ")

caminho_arquivo = os.path.join('files', nome_arquivo)

if os.path.isfile(caminho_arquivo):
    nome, _ = os.path.splitext(nome_arquivo)
    
    novo_nome_arquivo = f"{nome}_cópia.txt"
    caminho_novo_arquivo = os.path.join('files', novo_nome_arquivo)
    
    shutil.copy(caminho_arquivo, caminho_novo_arquivo)
    
    print(f"O arquivo {nome_arquivo} foi copiado para {novo_nome_arquivo}.")
else:
    print("Arquivo não encontrado.")

