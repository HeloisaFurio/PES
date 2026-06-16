cod=int(input("Insira o código do produto(de 1 á 8): "))
quant=int(input("Quantos desse produto foram comprados? "))

if cod==1:
    produto="suco"
    valor=6
    valor*=quant
    print(f"Você comprou {produto} e custou R${valor}.")