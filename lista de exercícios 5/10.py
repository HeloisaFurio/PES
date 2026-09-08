import random

def embaralhar_string(texto):
    texto = texto.lower()
    caracteres = list(texto)
    random.shuffle(caracteres)
    return "".join(caracteres)

palavra = input("Digite uma palavra: ")
print("Embaralhada:", embaralhar_string(palavra))