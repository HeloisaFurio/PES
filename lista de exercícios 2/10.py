n= int(input("Insira um numero inteiro de sua preferencia: "))
soma = n
cont = 1
while n != 0:
    n = int(input("Insira outro numero inteiro de sua preferencia: "))
    cont += 1
    soma += n

cont -= 1

media = soma/cont
print("0 é o único número proibido.🫵​🤣​")
print(f"Você inseriu {cont} números, a soma deles é = {soma} e a média é = {media}")
