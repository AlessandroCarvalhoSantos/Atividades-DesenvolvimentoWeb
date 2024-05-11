# Crie um arquivo vazio qualquer. Agora, na mesma pasta, crie um programa que 
# solicite ao usuário que digite o nome desse arquivo e exclua-o. 

import os

with open('files/exemplo.txt', 'w') as arquivo:
    pass  


nome_arquivo = input("Digite o nome do arquivo a ser excluído (com extensão): ")

caminho_arquivo = os.path.join('files', nome_arquivo)

if os.path.isfile(caminho_arquivo):
    os.remove(caminho_arquivo)
    print(f"O arquivo {nome_arquivo} foi excluído.")
else:
    print("Arquivo não encontrado.")
