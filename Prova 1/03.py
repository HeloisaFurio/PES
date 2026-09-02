dicionario = {}

quant = int(input("Quantas palavras você quer adicionar?\n- "))
i=0

while i < quant:
    palavra = input("Insira a palavra:\n- ")
    significado = input("Insira o siginificado dela:\n- ")
    dicionario[palavra] = significado
    print("Palavra cadastrada com sucesso!")
    i+=1


for palavra, significado in dicionario.items():
    print(f"{palavra} : {significado}")
    