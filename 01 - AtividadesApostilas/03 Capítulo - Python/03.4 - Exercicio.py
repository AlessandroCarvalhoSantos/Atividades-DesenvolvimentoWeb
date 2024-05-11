#Crie um programa que verifique se um número digitado pelo usuário é perfeito.

def eh_perfeito(n):
    if n <= 1:
        return False
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    return soma_divisores == n

numero = int(input("Digite um número para verificar se é perfeito: "))

if eh_perfeito(numero):
    print(f"O número {numero} é perfeito.")
else:
    print(f"O número {numero} não é perfeito.")
