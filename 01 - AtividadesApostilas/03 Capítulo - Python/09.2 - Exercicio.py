# Crie uma função que leia um arquivo de texto e exiba o conteúdo na tela. Trate exceções 
# caso o arquivo não exista ou não seja possível lê-lo. 

def ler_arquivo(nome_arquivo):
    try:
        with open("files/"+nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except IOError:
        print(f"Erro: Não foi possível ler o arquivo '{nome_arquivo}'.")

nome_arquivo = input("Digite o nome do arquivo a ser lido (com extensão): ")

ler_arquivo(nome_arquivo)
