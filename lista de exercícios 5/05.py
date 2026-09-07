def lista_vazia(lista):
    if lista == []:
        return "True"
    else:
        return "False"
    
def maior_lista(lista):
    if lista == []:
        return "A lista está vazia\n -1"
    else:
        maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior

def menor_lista(lista):
    if lista == []:
        return "A lista está vazia\n -1"
    else:
        menor = lista[0]
        for n in lista:
            if n < menor:
                menor = n
        return menor

def media_lista(lista):
    if lista == []:
        return "A lista está vazia\n -1"
    else:
        soma = 0
        for n in lista:
            soma += n
    media = soma / len(lista)
    return media

listaVazia = []
listaCheia = [0, 1, 2, 3, 4, 5]

listaEscolhida = input("Qual lista você deseja utilizar? (Digite 'vazia' ou 'cheia'): ")

if listaEscolhida == "vazia":
    lista = listaVazia
elif listaEscolhida == "cheia":
    lista = listaCheia
else:
    print("Opção inválida")

if lista_vazia(lista) == "True":
    print("A lista está vazia")
    
else:
    print("A lista não está vazia")
    print(f"O maior número da lista é: {maior_lista(lista)}")
    print(f"O menor número da lista é: {menor_lista(lista)}")
    print(f"A média dos números da lista é: {media_lista(lista)}")
    