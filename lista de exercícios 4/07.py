notas = []


opcao_escolhida = -1
while opcao_escolhida != 0:
    print("""Notas
        -----
        1 - Cadastrar
        2 - Excluir
        3 - Listar
        4 - Calcular média
        5 – Mostrar maior nota
        6 – Mostrar menor nota
        0 - Sair""")
    opcao_escolhida = int(input("Digite sua opcão: "))
    i=0
    if opcao_escolhida == 1:
        print("Cadastrar")
        notas.append(int(input("Digite sua nota:  ")))
        print("Cadastrado com sucesso!")

    elif opcao_escolhida == 2:
        print("Excluir")
        i = 0
        while i<len(notas):
            print(f"{i}--    {notas[i]}")
            i+=1
        j = int(input("Que nota você deseja excluir? (informe apenas a posição) "))
        notas.pop(j)
        print("Nota deletada com sucesso!")
        
    elif opcao_escolhida == 3:
        print("Listar")
        if len(notas) == 0:
            print("A lista está vazia, cadastre alguma nota.")
        else:
            i = 0
            while i<len(notas):
                print(f"{i}    {notas[i]}")
                i+=1

    elif opcao_escolhida == 4:
        print("Calculando...")
        i = 0
        soma = 0
        while i < len(notas):
            soma+= notas[i]
            i+=1
        media=soma/(i)
        print(f"Sua média é de {media}")
    
    elif opcao_escolhida == 5:
        print("Procurando...")
        if len(notas) == 0:
            print("“Erro: não há notas cadastradas.")
        else:
            maior = max(notas)
            print(f"Sua maior nota é {maior}")
    
    elif opcao_escolhida == 6:
        print("Procurando...")
        if len(notas) == 0:
            print("“Erro: não há notas cadastradas.")
        else:
            menor = min(notas)
            print(f"Sua menor nota é {menor}")