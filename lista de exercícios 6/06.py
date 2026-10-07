class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso 

    def exibir(self):
        return f"Nome: {self.nome} | Idade: {self.idade} anos| Altura: {self.altura}m | Peso: {self.peso}Kg"

lista_pessoa = []

opcao_escolhida = -1
while opcao_escolhida != 0:
    print("""Menu
--------------
1 – Cadastrar
2 - Listar
0 - Sair""")
    opcao_escolhida = int(input("Digite sua opcão: "))

    if opcao_escolhida == 1:
        print("Cadastrar...")
        lista_pessoa.append(Pessoa(input("Nome: "), (input("Idade: ")), (input("Altura: ")), (input("Peso: "))))
        
    elif opcao_escolhida == 2:
        print("Listar...")
        for pessoa in lista_pessoa:
            print(pessoa.exibir())