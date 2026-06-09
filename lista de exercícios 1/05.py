temp = float(input("Qual a atemperatura de hoje? "))#.replace(",", "."))
if temp < 10:
    print("Está muito frio! Use roupas quentes.")
elif temp >= 10 and temp <=20:
    print("Frio. Vista-se bem!")
elif 20<temp and temp <= 25:
    print("Temperatura agradável.")
elif 25<temp and temp <=30:
    print("Está ficando quente!")
elif temp>30:
    print("Está muito quente! Fique hidratado.")