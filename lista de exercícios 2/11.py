cod=int(input("Insira o código do produto(de 1 á 8): "))
quant=int(input("Quantos desse produto foram comprados? "))

if cod==1:
    produto="suco"
    valor=6
    valor*=quant
    print(f"Você comprou {quant} suco(s) e custou R${valor}.")
elif cod==2:
    valor=3
    valor*=quant
    print(f"Você comprou {quant} pão(es) de queijo e custou R${valor}.")
elif cod==3:
    valor=7
    valor*=quant
    print(f"Você comprou {quant} pastel(is) e custou R${valor}.")
elif cod==4:
    valor=9
    valor*=quant
    print(f"Você comprou {quant} salada(s) de frutas e custou R${valor}.")
elif cod==5:
    valor=3.50
    valor*=quant
    print(f"Você comprou {quant} café(s) com leite e custou R${valor}.")
elif cod==6:
    valor=4.50
    valor*=quant
    print(f"Você comprou {quant} cappuccino(s) e custou R${valor}.")
elif cod==7:
    valor=6.50
    valor*=quant
    print(f"Você comprou {quant} iogurte(s) e custou R${valor}.")
elif cod==8:
    valor=2.50
    valor*=quant
    print(f"Você comprou {quant} água(s) e custou R${valor}.")