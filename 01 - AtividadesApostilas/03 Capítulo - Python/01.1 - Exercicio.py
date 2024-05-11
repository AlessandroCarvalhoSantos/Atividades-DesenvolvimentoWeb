#Crie um programa que peça ao usuário para digitar um número. 
#Em seguida, o programa deve calcular e mostrar a raiz quadrada desse número.

import math
numero = float(input("Digite um número para calcular a raiz quadrada: "))

if numero < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
else:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
