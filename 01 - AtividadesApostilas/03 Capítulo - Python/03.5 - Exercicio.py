#Crie um programa que encontre e mostre o maior e o menor número em uma lista de 10 
#números digitada pelo usuário.

numeros = []

print("Digite 10 números:")

for i in range(10):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número digitado é: {maior_numero}")
print(f"O menor número digitado é: {menor_numero}")
