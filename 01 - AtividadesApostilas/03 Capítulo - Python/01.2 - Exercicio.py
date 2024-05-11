#Crie um programa que peça ao usuário para digitar o raio de um círculo. 
#Em seguida, o programa deve calcular e mostrar a área e o comprimento do círculo.

import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio ** 2

comprimento = 2 * math.pi * raio

print(f"A área do círculo com raio {raio} é {area:.2f}")
print(f"O comprimento do círculo com raio {raio} é {comprimento:.2f}")
