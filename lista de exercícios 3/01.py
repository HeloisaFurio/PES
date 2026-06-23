idades = [0]*6
i=0

while i < 6:
    idades[i] =  int(input(f"Insira a idade do aluno{i}: "))
    i += 1

i=0
if idades[i] >= 16:
    print (f"O aluno{i} tem mais de 16 anos, ele tem {idades[i]} anos.")
    i += 1