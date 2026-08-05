bairros = []

bairros.append("Centro")

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
        bairros.append(input("Digite os bairros de Garopaba:  "))

    elif opcao_escolhida == 2:
        print("Excluir")
        i = 0
        while i<len(bairros):
            print(f"{i}    {bairros[i]}")
            i+=1
        j = int(input("Qual bairro você deseja excluir? (informe apenas a posição) "))
        bairros.pop(j)
        print("Bairro deletado com sucesso!")
        
    elif opcao_escolhida == 3:
        print("Listar")
        i = 0
        while i<len(bairros):
            print(f"{i}    {bairros[i]}")
            i+=1