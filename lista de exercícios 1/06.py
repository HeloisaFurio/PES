print("Vamos jogar Pedra, Papel, Tesoura!! :º")

nome1 = input("Insira o nome do jogador 1: ")
nome2 = input("Insira o nome do jogador 2: ")

print("Vamos começar!")

jogador1 = int(input(f"{nome1}, digite 1 para pedra, 2 para papel ou 3 para tesoura: "))
jogador2 = int(input(f"{nome2}, digite 1 para pedra, 2 para papel ou 3 para tesoura: "))

if jogador1==1 and jogador2==2 or jogador1==2 and jogador2==3 or jogador1==3 and jogador2==1:
    print (f"Parabéns! {nome2} venceu!")
else:
    print (f"Parabéns! {nome1} venceu!")