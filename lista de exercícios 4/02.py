notas = []

j = int(input("Quantas notas você tem?  "))

for i in range(j):
    nota = int(input(f"Qual sua nota 0{i+1}? "))
    notas.append(nota)
i=0
while i<len(notas):
    print(f"{notas[i]}")
    i+=1