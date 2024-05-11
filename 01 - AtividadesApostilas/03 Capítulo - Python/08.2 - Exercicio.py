# Crie uma classe chamada Carro com o atributo velocidade e com métodos 
# para acelerar e frear o carro por X segundos, sendo que o carro acelera a 
# 10m/s2 e freia a 5m/s2. Crie uma instância da classe Carro e teste os métodos criados. 


class Carro:
    def __init__(self):
        self.velocidade = 0  

    def acelerar(self, segundos):
        aceleracao = 10  
        self.velocidade += aceleracao * segundos
        print(f"O carro acelerou por {segundos} segundos. Velocidade atual: {self.velocidade} m/s")

    def frear(self, segundos):
        desaceleracao = 5  
        self.velocidade -= desaceleracao * segundos
        if self.velocidade < 0:
            self.velocidade = 0  
        print(f"O carro freou por {segundos} segundos. Velocidade atual: {self.velocidade} m/s")

meu_carro = Carro()

meu_carro.acelerar(5) 
meu_carro.frear(2)     
meu_carro.acelerar(3)  
meu_carro.frear(10)    
