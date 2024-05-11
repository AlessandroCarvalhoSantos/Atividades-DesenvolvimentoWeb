# Crie uma função de ordem superior chamada transformarLista que aceite uma lista de 
# números inteiros e uma função como parâmetros. Aplique a função do parâmetro a 
# cada um dos elementos da lista passada como argumento, retornando uma nova lista 
# de mesmo tamanho, porém, com os elementos transformados. Agora crie uma função chamada 
# porExtenso que receba um número inteiro entre 0 e 9 como argumento e retorne seu nome por extenso. 
# Para concluir, chame a função transformarLista passando [1, 2, 3, 4, 5] como primeiro argumento e a 
# função porExtenso como segundo argumento, mostrando a lista resultante.


def transformarLista(lista, func):
    return [func(elemento) for elemento in lista]

def porExtenso(numero):
    nomes_por_extenso = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    if 0 <= numero <= 9:
        return nomes_por_extenso[numero]
    else:
        return "Número fora do intervalo"

lista_resultante = transformarLista([1, 2, 3, 4, 5], porExtenso)
print(lista_resultante)
