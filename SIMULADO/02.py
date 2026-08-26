cartela_bingo = []

for i in range(15):
    numero = int(input(f"Insira o número {i+1} da cartela: \n- "))

    if (numero <= 75 and numero >= 1) and not numero in cartela_bingo:
        cartela_bingo.append(numero)
    else:
        print("Erro! Número inválido, o número deve estar entre 1 e 75")
        numero = int(input(f"Insira o número {i+1} da cartela: \n- "))
        cartela_bingo.append(numero)
    
# maior = cartela_bingo[0]
# i = 1
# while i < len(cartela_bingo):
#     if maior < cartela_bingo[i]:
#         maior = cartela_bingo[i-1]
#         cartela_bingo[i-1] = cartela_bingo[i]
#         cartela_bingo[i] = maior
#     i+=1

cartela_bingo.sort()

i=0
while i < len(cartela_bingo):
    print(cartela_bingo[i])
    i+= 1