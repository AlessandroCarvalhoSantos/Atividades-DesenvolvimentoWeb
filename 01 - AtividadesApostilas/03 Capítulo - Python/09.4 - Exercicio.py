# Crie uma classe Triangulo com os atributos lado1, lado2 e lado3. Implemente um 
# método tipo_triangulo que informe se o triângulo é equilátero, isósceles ou escaleno. 
# Utilize tratamento de exceções para lidar com triângulos inválidos. 

class TrianguloInvalidoError(Exception):
    """Triângulos inválidos."""
    pass

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

        if not self._valida_triangulo():
            raise TrianguloInvalidoError("Os lados fornecidos não formam um triângulo válido.")

    def _valida_triangulo(self):
        """Verifica se os lados formam um triângulo válido."""
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

    def tipo_triangulo(self):
        """Determina o tipo do triângulo."""
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

try:
    t1 = Triangulo(3, 4, 5)
    print(f"Triângulo com lados 3, 4 e 5 é {t1.tipo_triangulo()}.")
    
    t2 = Triangulo(3, 3, 3)
    print(f"Triângulo com lados 3, 3 e 3 é {t2.tipo_triangulo()}.")
    
    t3 = Triangulo(3, 3, 5)
    print(f"Triângulo com lados 3, 3 e 5 é {t3.tipo_triangulo()}.")

    t4 = Triangulo(1, 2, 3)  # Triângulo inválido
    print(f"Triângulo com lados 1, 2 e 3 é {t4.tipo_triangulo()}.")
except TrianguloInvalidoError as e:
    print(e)
