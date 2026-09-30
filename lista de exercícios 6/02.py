class Carro: 
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def pintar(self):
        cornew = input("Insira a nova cor: ")
        self.cor = cornew

    def mostrar_cor(self):
        print(f"A cor atual do carro é {self.cor}")

bmw = Carro("BMW", "roxo")

bmw.pintar()
bmw.mostrar_cor()