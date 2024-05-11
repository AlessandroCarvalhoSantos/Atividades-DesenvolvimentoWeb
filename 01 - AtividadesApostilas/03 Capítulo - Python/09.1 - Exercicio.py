# Crie uma classe chamada ContaBancaria com os métodos depositar e sacar. Utilize tratamento 
# de exceções para lidar com saques maiores que o saldo disponível, criando uma exceção personalizada. 

class SaldoInsuficienteError(Exception):
    """Saldo insuficiente."""
    pass

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
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

conta = ContaBancaria()

try:
    conta.depositar(1000)
    conta.exibir_saldo()

    conta.sacar(200)
    conta.exibir_saldo()

    conta.sacar(900)  
    conta.exibir_saldo()
except SaldoInsuficienteError as e:
    print(e)

try:
    conta.sacar(-50)  
    conta.exibir_saldo()
except SaldoInsuficienteError as e:
    print(e)

try:
    conta.sacar(100)  
    conta.exibir_saldo()
except SaldoInsuficienteError as e:
    print(e)
