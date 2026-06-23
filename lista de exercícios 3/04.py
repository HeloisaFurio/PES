lista = [-1]*15

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
        print("Criando")

        #substituir o valor se possível
        lugar_livre = 0
        for lugar in lista:
            if lugar < 0:
                break
            lugar_livre = lugar_livre + 1
 
        if lugar_livre > len(lista):
            print("Não posso cadastrar!")
        else:
            print(f"Tem um espaço no {lugar_livre}")

            lista[lugar_livre] = int(input("Digite sua placa: "))
            
    elif opcao_escolhida == 2:
        print("Excluir")
        
    elif opcao_escolhida == 3:
        print("Listar")
        for placa in lista:
            if placa > 0:
                print(f"Item com placa: {placa}")
   