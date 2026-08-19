
notas = []
soma = 0
def media ():
    for i in range(3):
        nota = int(input(f"Qual sua nota 0{i+1}? "))
        notas.append(nota)
        soma += nota
    media=soma/3

    

print(f"Sua média é {media: .2f}")