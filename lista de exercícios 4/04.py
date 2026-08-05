cidades = []

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
        cidades.append(input("Digite a cidade:  "))

    elif opcao_escolhida == 2:
        print("Excluir")
        i = 0
        while i<len(cidades):
            print(f"{i}    {cidades[i]}")
            i+=1
        j = int(input("Que cidade você deseja excluir? (informe apenas a posição) "))
        cidades.pop(j)
        print("Cidade deletada com sucesso!")
        
    elif opcao_escolhida == 3:
        print("Listar")
        i = 0
        while i<len(cidades):
            print(f"{i}    {cidades[i]}")
            i+=1