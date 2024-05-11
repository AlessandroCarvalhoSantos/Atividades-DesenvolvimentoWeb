# Crie um programa que declare uma lista chamada idades com 
# 5 números inteiros. Logo em seguida, crie uma função chamada 
# adicionar que receba uma lista como parâmetro e que adicione um 
# novo elemento qualquer a essa lista. Feito isso, chame a função adicionar passando a 
# lista idades como argumento. Por fim, após a chamada da função, mostre a lista idades para 
# verificar se o elemento foi adicionado corretamente.

idades = [10, 20, 30, 40, 50]

def adicionar(lista):
    lista.append(60)

adicionar(idades)

print(idades)
