class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso 

    def exibir(self):
        return f"Nome: {self.nome} | Idade: {self.idade} anos| Altura: {self.altura}m | Peso: {self.peso}Kg"
    
class Professor:
    def __init__(self, matricula: int, nome: str, sobrenome: str, idade: int, especializacao: str):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.especializacao = especializacao 

    def apresentar(self):
        return f"Nome: {self.nome} | Idade: {self.idade} anos| Altura: {self.altura}m | Peso: {self.peso}Kg"
lista_pessoa = []

opcao_escolhida = -1
while opcao_escolhida != 0:
    print("""Menu
--------------
1 – Cadastrar
2 – Listar
3 – Excluir
4 – Alterar 
0 - Sair""")
    opcao_escolhida = int(input("Digite sua opcão: "))

    if opcao_escolhida == 1:
        print("Cadastrar:")
        nome = input("Nome: ") 
        idade = int(input("Idade: ")) 
        altura = float(input("Altura: ")) 
        peso = float(input("Peso: "))
        lista_pessoa.append(Pessoa(nome, idade, altura, peso))
        print("Pessoa cadastrada com sucesso!")
        
    elif opcao_escolhida == 2:
        print("Listar:")
        for pessoa in lista_pessoa:
            print(pessoa.exibir())

    elif opcao_escolhida == 3:
        print("Escluir:")
        for pessoa in lista_pessoa:
            print(pessoa.exibir())
        nomeAExcluir = input("Quem você deseja exluir?\n- ")
        for pessoa in lista_pessoa:
            if pessoa.nome == nome:
                lista_pessoa.remove(pessoa)
                print("Pessoa deletada com sucesso!")
                break
        

    elif opcao_escolhida == 4:
        print("Alterar:")
        for pessoa in lista_pessoa:
            print(pessoa.exibir())
        nome = input("Quem você deseja alterar?\n- ")
        for pessoa in lista_pessoa:
            if pessoa.nome == nome:
                pessoa.idade = int(input("Insira a nova idade: ")) 
                pessoa.altura = float(input("Insira a nova altura: ")) 
                pessoa.peso = float(input("Insira o novo peso: ")) 
                print("Dados alterados com sucesso!")
                break