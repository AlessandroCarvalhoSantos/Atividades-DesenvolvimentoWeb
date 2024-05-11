# Crie uma classe chamada Retangulo com um método __init__ que inicialize a largura e a 
# altura do retângulo. Crie um método chamado area que retorne a área do retângulo. Crie 
# uma classe chamada Quadrado que herde da classe Retangulo e substitua o método __init__ para 
# que seja necessário apenas informar um lado, ao invés de largura e altura. Crie uma instância da 
# classe Quadrado e chame o método area.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

quadrado = Quadrado(5)

area_quadrado = quadrado.area()
print(f"A área do quadrado é: {area_quadrado}")
