placas = []

opcao = -1

while opcao != 0:
    print('''Menu:
1 - Cadastrar
2 - Excluir
3 - Listar
0 - Sair''')
    opcao = int(input("Escolha uma opção: \n- "))
    print("\n")

    if opcao == 1:
        print("Cadastro")
        placa = input("Insira a placa: \n- ")
        print("\n"
        placas.append(placa)

    elif opcao == 2:
        print("Excluir")
        placa_excluir = input("Qual placa deseja excluir?\n- ")
        placas.remove(placa_excluir)
        print("Placa deletada com sucesso!\n")

    elif opcao == 3:
        for placa in placas:
            print(placa)
            print("\n")

    elif opcao == 0:
        print("Encerrando...")

    else:
        print("Opção inválida.")
        print("\n")