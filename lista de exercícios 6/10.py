import pickle

class Estudante:
    def __init__(self, matricula: int, nome: str, sobrenome: str, idade: int, ):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade 

    def apresentar(self):
        return f"Matrícula: {self.matricula} | Nome: {self.nome} | Sobrenome: {self.sobrenome} | Idade: {self.idade} anos"
    
class Professor:
    def __init__(self, matricula: int, nome: str, sobrenome: str, idade: int, especializacao: str):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.especializacao = especializacao 

    def apresentar(self):
        return f"Matrícula: {self.matricula} | Nome: {self.nome} | Sobrenome: {self.sobrenome} | Idade: {self.idade} anos | Especialização: {self.especializacao}"
lista_estudante = []
lista_professor = []

###############################################################################################################################################################################

opcao_escolhida = -1
while opcao_escolhida != 0:
    print("""Menu
--------------
01 – Cadastrar estudante
02 – Cadastrar professor
03 – Listar estudantes
04 – Listar professores
05 – Alterar estudante pela matrícula
06 – Alterar estudante pelo nome
07 – Alterar professor pela matrícula
08 – Alterar professor pelo nome 
09 – Excluir estudante pela matrícula
10 – Excluir professor pela matrícula
11 – Salvar dados
12 – Carregar dados
00 – Sair""")
    opcao_escolhida = int(input("Digite sua opcão: "))

    if opcao_escolhida == 1:
        print("Cadastrar estudante:")
        matricula = int(input("Matrícula: ")) 
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = int(input("Idade: ")) 
        
        lista_estudante.append(Estudante(matricula, nome, sobrenome, idade))
        print("Estudante cadastrado com sucesso!")

    elif opcao_escolhida == 2:
        print("Cadastrar professor:")
        matricula = int(input("Matrícula: ")) 
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = int(input("Idade: "))
        especializacao = input("Especialização: ") 
        
        lista_professor.append(Professor(matricula, nome, sobrenome, idade, especializacao))
        print("Professor cadastrado com sucesso!")
        
    elif opcao_escolhida == 3:
        print("Listar estudantes:")
        for estudante in lista_estudante:
            print(estudante.apresentar())

    elif opcao_escolhida == 4:
        print("Listar professores:")
        for professor in lista_professor:
            print(professor.apresentar())

    elif opcao_escolhida == 5:
        print("Alterar estudante pela matrícula:")
        for estudante in lista_estudante:
            print(estudante.apresentar())
        matriculaAAlterar = int(input("Quem você deseja alterar?\n- "))
        for estudante in lista_estudante:
            if estudante.matricula == matriculaAAlterar:
                estudante.nome = (input("Insira o novo nome: ")) 
                estudante.sobrenome = (input("Insira o novo sobrenome: ")) 
                estudante.idade = int(input("Insira a nova idade: ")) 
                print("Dados alterados com sucesso!")
                break


    elif opcao_escolhida == 6:
        print(" Alterar estudante pelo nome:")
        for estudante in lista_estudante:
            print(estudante.apresentar())
        nomeAAlterar = input("Quem você deseja alterar?\n- ")
        for estudante in lista_estudante:
            if estudante.nome == nomeAAlterar:
                estudante.matricula = int(input("Insira a nova matrícula: ")) 
                estudante.sobrenome = (input("Insira o novo sobrenome: ")) 
                estudante.idade = int(input("Insira a nova idade: ")) 
                print("Dados alterados com sucesso!")
                break

    elif opcao_escolhida == 7:
        print("Alterar professor pela matrícula:")
        for professor in lista_professor:
            print(professor.apresentar())
        matriculaAAlterar = int(input("Quem você deseja alterar?\n- "))
        for professor in lista_professor:
            if professor.matricula == matriculaAAlterar:
                professor.nome = input("Insira o novo nome: ")
                professor.sobrenome = input("Insira o novo sobrenome: ")
                professor.idade = int(input("Insira a nova idade: "))
                professor.especializacao = input("Insira a nova especialização: ")
                print("Dados alterados com sucesso!")
                break

    elif opcao_escolhida == 8:
        print("Alterar professor pelo nome:")
        for professor in lista_professor:
            print(professor.apresentar())
        nomeAAlterar = input("Quem você deseja alterar?\n- ")
        for professor in lista_professor:
            if professor.nome == nomeAAlterar:
                professor.matricula = int(input("Insira a nova matrícula: ")) 
                professor.sobrenome = input("Insira o novo sobrenome: ")
                professor.idade = int(input("Insira a nova idade: "))
                professor.especializacao = input("Insira a nova especialização: ") 
                print("Dados alterados com sucesso!")
                break

    elif opcao_escolhida == 9:
        print("Excluir estudante pela matrícula:")
        for estudante in lista_estudante:
            print(estudante.apresentar())
        matriculaAExcluir = int(input("Quem você deseja exluir?\n- "))
        for estudante in lista_estudante:
            if estudante.matricula == matriculaAExcluir:
                lista_estudante.remove(estudante)
                print("Estudante deletado com sucesso!")
                break

    elif opcao_escolhida == 10:
        print("Excluir professor pela matrícula:")
        for professor in lista_professor:
            print(professor.apresentar())
        matriculaAExcluir = int(input("Quem você deseja exluir?\n- "))
        for professor in lista_professor:
            if professor.matricula == matriculaAExcluir:
                lista_professor.remove(professor)
                print("Professor deletado com sucesso!")
                break

    elif opcao_escolhida == 11:
        print("Salvar:")
        with open('dados.pkl', 'wb') as f:
            pickle.dump([lista_estudante, lista_professor], f)
            print("Dados salvos com sucesso!")

    elif opcao_escolhida == 12:
        print("Carregar:")
        with open('dados.pkl', 'rb') as f:
            listas = pickle.load(f)
            lista_estudante = listas[0]
            lista_professor = listas[1]
            print("Dados carregados com sucesso!")