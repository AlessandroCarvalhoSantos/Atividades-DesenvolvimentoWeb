# Crie um programa que exclua o diretório criado no exercício anterior 
# com todo o seu conteúdo (cuidado para não excluir a pasta errada).

import os
import shutil

pasta_files = 'files'

diretorio_temp = os.path.join(pasta_files, 'temp')

if os.path.isdir(diretorio_temp):
    shutil.rmtree(diretorio_temp)
    print(f"O diretório '{diretorio_temp}' e todo o seu conteúdo foram excluídos com sucesso.")
else:
    print("O diretório 'temp' não foi encontrado na pasta 'files'.")
