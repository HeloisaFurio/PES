
menu = """Menu
-------
1 – Adição
2 – Subtração
3 – Divisão
4 – Multiplicação
0 - Sair"""

tipo = 11
while tipo != 0:
    n1=int(input("Insira o primeiro número: "))
    n2=int(input("Insira o segundo número: "))
    print("\n")
    print(menu)
    tipo = int(input("Digite a opção: "))
    print("\n")

    if tipo == 1:
        valor = n1 + n2
        print(f"{n1} + {n2} = {valor}")
        print("\n\n")
    elif tipo == 2:
        valor = n1 - n2
        print(f"{n1} - {n2} = {valor}")
        print("\n\n")
    elif tipo == 3:
        valor = n1 * n2
        print(f"{n1} x {n2} = {valor}")
        print("\n\n")
    elif tipo == 4:
        valor = n1 / n2
        print(f"{n1} ÷ {n2} = {valor}")
        print("\n\n")
    else:
        int(input("Opção inválida"))