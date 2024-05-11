#Crie um programa que calcule e mostre a soma de todos os números primos de 1 a 100.

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

soma_primos = 0

for num in range(1, 101):
    if eh_primo(num):
        soma_primos += num

print(f"A soma de todos os números primos de 1 a 100 é: {soma_primos}")
