notas = []
soma = 0

for i in range(4):
    nota = int(input(f"Qual sua nota 0{i+1}? "))
    notas.append(nota)
    soma += nota

media=soma/4

if media < 6:
    print(f"Sua média é {media: .2f} e você reprovou de ano...😐​")
else:
    print(f"Sua média é {media: .2f} e você PASSOOOU DE ANOOOO!!😋​😋​😋​😋​")



# for i, nota in enumerate(notas):
#     if idade == 16:
#         print (f"O aluno{i+1} tem 16 anos, ele tem {idade} anos.")
#     elif idade > 16:
#         print (f"O aluno{i+1} tem mais de 16 anos, ele tem {idade} anos.")