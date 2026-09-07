def tempo_total(horas, minutos):
    total_minutos = (horas * 60) + minutos
    return total_minutos

horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
print(f"O tempo total que você passou jogando em minutos é: {tempo_total(horas, minutos)}")