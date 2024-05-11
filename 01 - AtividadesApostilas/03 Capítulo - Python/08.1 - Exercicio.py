# Crie uma classe chamada ContaBancaria com o atributo saldo e com métodos para depositar, 
# sacar e exibir o saldo da conta. Crie uma instância da classe ContaBancaria e teste os 
# métodos criados. 

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

conta = ContaBancaria()

conta.depositar(1000)
conta.exibir_saldo()

conta.sacar(200)
conta.exibir_saldo()

conta.sacar(900)
conta.exibir_saldo()

conta.depositar(-50)
conta.exibir_saldo()

conta.sacar(100)
conta.exibir_saldo()
