dicionario = {
    "apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados.",
}

for i in range(4):
    palavra = input("Insira a palavra:\n- ")
    dicionario[palavra] = input("Insira o significado dela:\n- ")

palavra = input("Qual palavra esta procurando?\n- ")
if palavra in dicionario:
    print (dicionario[palavra])
else:
    print("Palavra não cadastrada.")

