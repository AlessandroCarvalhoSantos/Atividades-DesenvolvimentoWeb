# Faça um programa que crie um diretório chamado "temp" e, dentro desse 
# diretório, crie também um arquivo chamado "temp.txt". 

import os

pasta_files = 'files'

diretorio_temp = os.path.join(pasta_files, 'temp')

os.makedirs(diretorio_temp, exist_ok=True)

arquivo_temp = os.path.join(diretorio_temp, 'temp.txt')

with open(arquivo_temp, 'w') as arquivo:
    arquivo.write('') 

print(f"Diretório '{diretorio_temp}' e arquivo '{arquivo_temp}' criados com sucesso.")


