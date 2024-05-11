# Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da 
# pessoa, e um método chamado mostrar_dados que exiba o nome e a idade da pessoa. Crie uma 
# classe chamada Aluno que herde da classe Pessoa e adicione um atributo matricula e um método 
# mostrar_dados que exiba o nome, a idade e a matrícula do aluno. Crie uma instância da classe 
# Aluno e chame o método mostrar_dados. 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Matrícula: {self.matricula}")

aluno = Aluno("Maria", 20, "123456")

aluno.mostrar_dados()
