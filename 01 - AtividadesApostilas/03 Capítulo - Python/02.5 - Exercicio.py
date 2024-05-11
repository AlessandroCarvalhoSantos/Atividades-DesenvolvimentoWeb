# Escreva um programa que peça ao usuário para inserir uma faixa etária e, 
# em seguida, utilize a estrutura match..case para sugerir um filme adequado 
# para essa idade. Você pode categorizar as faixas etárias e sugerir diferentes 
# tipos de filmes para cada categoria, como filmes infantis para crianças, ação para adolescentes, 
# drama para adultos etc.

idade = int(input("Digite sua idade: "))

match idade:
    case idade if idade < 12:
        sugestao = "Filme infantil: 'Toy Story'"
    case idade if 12 <= idade < 18:
        sugestao = "Filme de ação: 'Homem-Aranha'"
    case idade if 18 <= idade < 25:
        sugestao = "Filme de aventura: 'Os Vingadores'"
    case idade if 25 <= idade < 40:
        sugestao = "Filme de drama: 'A Procura da Felicidade'"
    case idade if 40 <= idade < 60:
        sugestao = "Filme de suspense: 'A Origem'"
    case idade if idade >= 60:
        sugestao = "Filme clássico: 'E o Vento Levou'"
    case _:
        sugestao = "Faixa etária não reconhecida."

print(sugestao)
