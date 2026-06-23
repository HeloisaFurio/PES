idades = []

for i in range(6):
    idade = (int(input(f"digite aluno{i+1}: ")))
    idades.append(idade)

for i, idade in enumerate(idades):
    if idade >= 16:
        print (f"O aluno{i+1} tem mais de 16 anos, ele tem {idade} anos.")



# i = 0
# while i < 6:
#     idades[i] =  int(input(f"Insira a idade do aluno{i}: "))
#     i += 1

# i=0
# if idades[i] >= 16:
#     print (f"O aluno{i} tem mais de 16 anos, ele tem {idades[i]} anos.")
#     i += 1