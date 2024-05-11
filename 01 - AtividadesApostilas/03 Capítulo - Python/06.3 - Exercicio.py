# Faça um programa que declare uma lista de 10 números e mostre os 5 primeiros elementos e os 
# 5 últimos elementos da lista separadamente. 

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

primeiros_5 = numeros[:5]
print("Os 5 primeiros elementos são:", primeiros_5)

ultimos_5 = numeros[-5:]
print("Os 5 últimos elementos são:", ultimos_5)
