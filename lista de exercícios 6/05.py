import math
class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso 

    def exibir(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} anos| Altura: {self.altura}m | Peso: {self.peso}Kg")

    def IMC(self):
        self.imc = self.peso/self.altura**2
        print(f"Seu IMC (Índice de Massa Corpórea) é: {self.imc: .2f}")

    def retornar(self):
        print(f"{self.nome} : {self.imc: .2f}")

helo = Pessoa("Heloisa", 16, 1.70, 58)
juh = Pessoa("Julia", 16, 1.71, 65)
luiz = Pessoa("Luiz", 16, 1.50, 20)

helo.exibir()
juh.exibir()
luiz.exibir()


helo.IMC()
juh.IMC()
luiz.IMC()


helo.retornar()
juh.retornar()
luiz.retornar()