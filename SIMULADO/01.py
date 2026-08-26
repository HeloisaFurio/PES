ano = int(input("Insira o ano que deseja descobrir se é bissexto ou não: \n- "))

if (ano % 4 == 0) or (ano % 400 == 0) and (ano % 100 != 0):
    print(f"{ano} é um ano bissexto!")

else:
    print(f"{ano} não é um ano bissexto.")