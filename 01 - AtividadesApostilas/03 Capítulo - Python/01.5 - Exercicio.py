#Crie um programa que peça ao usuário para digitar a velocidade inicial, 
#a velocidade final e o tempo de transição de uma velocidade para a outra. 
# Em seguida, o programa deve calcular e mostrar a aceleração.

velocidade_inicial = float(input("Digite a velocidade inicial do objeto em metros por segundo: "))
velocidade_final = float(input("Digite a velocidade final do objeto em metros por segundo: "))
tempo_transicao = float(input("Digite o tempo de transição entre as velocidades em segundos: "))

if tempo_transicao == 0:
    print("O tempo de transição não pode ser zero.")
else:
    aceleracao = (velocidade_final - velocidade_inicial) / tempo_transicao
    print(f"A aceleração do objeto é {aceleracao:.2f} metros por segundo ao quadrado.")

