n = int(input("Insira o número: "))
n1 = int(input("Insira o início da tabuada: "))
n2 = int(input("Insira o final da tabuada: "))
var = n1

while var < n2 + 1:
    produto = var*n
    print(f"{n} x {var} = {produto}")
    var = var + 1