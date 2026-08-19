def calcular(r, h):
    return 3.14 * (r*r) * h

r=float(input("Insira o valor do raio do cilindro(em metros): \n"))
h=float(input("Insira o valor da altura do cilindro(em metros): \n"))

resultado = calcular(r, h)
print(f"O volume é igual a: \n{round(resultado,2)}m²")