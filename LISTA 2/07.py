quant = int(input("Quantas notas registradas você tem? "))
n=1
soma=0

while n < quant + 1:
    nota= int(input(f"Qual sua nota{n}? "))
    soma += nota
    n+=1
media=soma/quant
print("Sua média é: ", media)