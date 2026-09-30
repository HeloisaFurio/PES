class Produto:
    def __init__(self, nome, quant):
        self.nome = nome
        self.quant = quant
    
    def esta_disponivel(self):
        if self.quant > 0:
            print(True) 
        else:
            print(False)
        
    def vender(self):
        self.quant -= 1

produ = Produto("Chocolate", 1)

produ.esta_disponivel()
produ.vender()
produ.esta_disponivel()