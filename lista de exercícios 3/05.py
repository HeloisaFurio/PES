nome = []
idade = []
altura = []
peso = []

opcao_escolhida = -1
while opcao_escolhida != 0:
    print("""Menu
        ----
        1 – Cadastrar
        2 - Excluir
        3 - Alterar
        4 - Listar
        0 - Sair""")
    opcao_escolhida = int(input("Digite sua opcão: "))

    if opcao_escolhida == 1:
        print("Cadastrar")

        nome.append((input("Digite o nome: ")))
        idade.append(int(input("Digite a idade: ")))
        altura.append(float(input("Digite a altura: ")))
        peso.append(float(input("Digite o peso (em kilos): ")))
            
    elif opcao_escolhida == 2:
        print("Excluir")
        i = 0
        for placa in lista:
            if placa > 0:
                print(f"Item com placa: posição {i} - placa {placa}")
                i+=1
        j = int(input("Qual placa você deseja excluir? (informe apenas a posição da placa) "))
        lista[j] = -1
        print("Placa deletada com sucesso!")

        
    elif opcao_escolhida == 3:
        print("Listar")
        i = 0
        for placa in lista:
            if placa > 0:
                print(f"Item com placa: {i} - {placa}")
                i+=1
   