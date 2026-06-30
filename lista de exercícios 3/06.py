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
        while i<len(nome):
            print(f"{i}    {nome[i]}    {idade[i]}    {altura[i]}    {peso[i]}")
            i+=1
        j = int(input("Quem você deseja excluir? (informe apenas a posição) "))
        nome.pop(j)
        idade.pop(j)
        altura.pop(j)
        peso.pop(j)
        print("Usuario deletado com sucesso!")


    elif opcao_escolhida == 3:
        print("Alterar")
        i = 0
        while i<len(nome):
            print(f"{i}    {nome[i]}    {idade[i]}    {altura[i]}    {peso[i]}")
            i+=1
        j = int(input("Quem você deseja alterar? (informe apenas a posição) "))
        idade[j]=(input("Qual a nova idade?  "))
        altura[j]=(input("Qual a nova altura?  "))
        peso[j]=(input("Qual o novo peso?  "))
        
    elif opcao_escolhida == 4:
        print("Listar")
        i = 0
        while i<len(nome):
            print(f"{i}    {nome[i]}    {idade[i]}    {altura[i]}    {peso[i]}")
            i+=1
   