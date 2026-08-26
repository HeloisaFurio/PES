
opcao_escolhida = -1

while opcao_escolhida != 0:
    print('''• 1 – Adição;
• 2 – Subtração;
• 3 – Multiplicação;
• 4 – Divisão;
• 0 – Sair.''')
    opcao_escolhida = int(input("Insira uma opção:\n- "))
    print("\n")
    
    if opcao_escolhida == 1:
        n1 = int(input("Insira o número 1:\n- "))
        n2 = int(input("Insira o número 2:\n- "))
        soma = n1 + n2
        print(f"RESULTADO: {n1} + {n2} = {soma}\n")

    elif opcao_escolhida == 2:
        n1 = int(input("Insira o número 1:\n- "))
        n2 = int(input("Insira o número 2:\n- "))
        menos = n1 - n2
        print(f"RESULTADO: {n1} - {n2} = {menos}\n")

    elif opcao_escolhida == 3:
        n1 = int(input("Insira o número 1:\n- "))
        n2 = int(input("Insira o número 2:\n- "))
        vezes = n1 * n2
        print(f"RESULTADO: {n1} x {n2} = {vezes}\n")

    elif opcao_escolhida == 4:
        n1 = int(input("Insira o número 1:\n- "))
        n2 = int(input("Insira o número 2:\n- "))
        div = n1 / n2
        print(f"RESULTADO: {n1} ÷ {n2} = {div}\n")

    elif (opcao_escolhida < 0) or (opcao_escolhida > 4):
        print("Erro. Opção inválida.\n")

    else:
        print("Encerrando...")