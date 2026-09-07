def calcular(lista_recebida):
    n_somados = 0
    for n in lista_recebida:
        n_somados += n
    return n_somados

lista = []
for i in range(4):
    n = int(input("Digite um número: "))
    lista.append(n)

print(f"A soma dos números é: {calcular(lista)}")