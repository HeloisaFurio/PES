amgs = []

opcao_escolhida = -1
while opcao_escolhida != 0:
    print("""Menu
        ----
        1 – Cadastrar
        2 - Excluir
        3 - Listar
        0 - Sair""")
    opcao_escolhida = int(input("Digite sua opcão: "))

    if opcao_escolhida == 1:
        print("Cadastrar")
        amgs.append(input("Digite quem você quer adicionar:  "))

    elif opcao_escolhida == 2:
        print("Excluir")
        i = 0
        while i<len(amgs):
            print(f"{i}    {amgs[i]}")
            i+=1
        j = int(input("Quem você deseja excluir? (informe apenas a posição) "))
        amgs.pop(j)
        print("Amigo deletado com sucesso!")
        
    elif opcao_escolhida == 3:
        print("Listar")
        if len(amgs) == 0:
            print("A lista está vazia, cadastre algum amigo.")
        else:
            i = 0
            while i<len(amgs):
                print(f"{i}    {amgs[i]}")
                i+=1