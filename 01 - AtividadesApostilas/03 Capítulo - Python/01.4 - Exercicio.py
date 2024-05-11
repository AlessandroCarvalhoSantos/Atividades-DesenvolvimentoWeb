#Crie um programa que peça ao usuário para digitar a massa e a 
#aceleração de um objeto. Em seguida, o programa deve calcular e mostrar a força resultante.

massa = float(input("Digite a massa do objeto em quilogramas: "))
aceleracao = float(input("Digite a aceleração do objeto em metros por segundo ao quadrado: "))

forca = massa * aceleracao

print(f"A força resultante é {forca:.2f} Newtons.")
