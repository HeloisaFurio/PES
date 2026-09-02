def distancia_total(km, m):
    resultado = km * 1000
    resultado = resultado + m
    return (resultado)

km = int(input("Insira quantos quilômetros você percorreu(número inteiro):\n- "))
m = int(input("Insira quanto METROS você percorreu(número inteiro):\n- "))

print(f"Você percorreu {distancia_total(km, m)} metros")
