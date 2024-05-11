# Faça um programa que declare uma lista com ao menos 10 números inteiros, com pelo menos 3 
# deles repetidos. Em seguida, converta essa lista para um conjunto, visando eliminar os itens repetidos, 
# converta de volta para uma lista, e mostre o resultado na tela. 


numeros = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 3]

numeros_sem_repeticao = set(numeros)

lista_sem_repeticao = list(numeros_sem_repeticao)

print(lista_sem_repeticao)
