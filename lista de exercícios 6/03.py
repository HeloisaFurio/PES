class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        adicionar = int(input("Quantos reais você quer adicionar?\n- "))
        self.saldo += adicionar

    def sacar(self):
        saque = int(input("Quanto você quer sacar?\n- "))
        self.saldo -= saque

    def mostrar_saldo(self):
        print(f"O saldo é de R${self.saldo}")
    
conta = ContaBancaria("Heloisa", 1200)

conta.depositar()
conta.sacar()
conta.mostrar_saldo()