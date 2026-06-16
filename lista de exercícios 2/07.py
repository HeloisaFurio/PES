quant = int(input("Quantas notas registradas você tem? "))
n=1
soma=0

while n < quant + 1:
    nota= int(input(f"Qual sua nota{n}? "))
    soma += nota
    n+=1
media=soma/quant

if media < 6:
    print(f"Sua média é {media: .2f} e você reprovou de ano...😐​")
else:
    print(f"Sua média é {media: .2f} e você PASSOOOU DE ANOOOO!!😋​😋​😋​😋​")