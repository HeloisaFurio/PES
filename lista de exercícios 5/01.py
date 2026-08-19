def calcular(n1, n2, n3):
    media=(n1+n2+n3)/3
    return media
     
notas = []
for i in range(3):
    nota = int(input(f"Qual sua nota 0{i+1}? "))
    notas.append(nota)

resultado = calcular(notas[0], notas[1], notas[2])
print(f"Sua média é {resultado: .2f}")


# def media_lista(lista_recebida):
#     notas_somadas = 0
#     for nota in lista_recebida:
#         notas_somadas += nota

#     tamanho_lista = len(lista_recebida)

#     return notas_somadas/tamanho_lista

# notas = []
# for i in range(5):
#     nota = int(input(f"Qual sua nota 0{i+1}? "))
#     notas.append(nota)

# resultado = media_lista(notas)
# print(f"Sua média é {resultado: .2f}")