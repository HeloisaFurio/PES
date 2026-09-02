opcao = -1

while opcao != 0:
    print('''Menu:
1 - Login
0 - Sair''')
    opcao = int(input("Escolha uma opção: \n- "))
    print("\n")

    if opcao == 1:
        print("Login")
        user = input("Insira o nome de usuário: \n- ")
        senha = int(input("Insira a senha: \n- "))

        if (user == "admin") and (senha == 12345):
            print("Login bem-sucedido!")
            print("\n")

        else:
            print("Nome de usuário ou senha incorretos.")
            print("\n")

    elif opcao == 0:
        print("Encerrando...")

    else:
        print("Opção inválida.")
        print("\n")