def converter_hora(horario):
    hora, minuto = horario.split(":")
    hora = int(hora)

    if hora == 0:
        hora = 12
        periodo = "A"
    elif hora < 12:
        periodo = "A"
    elif hora == 12:
        periodo = "P"
    else:
        hora = hora - 12
        periodo = "P"


    return f"{hora}:{minuto}", periodo


def imprimir_saida(hora, periodo):
    if periodo == "A":
        print(hora, "A.M.")
    else:
        print(hora, "P.M.")


while True:
    horario = input("Digite a hora no formato 24h (HH:MM): ")

    hora_convertida, periodo = converter_hora(horario)
    imprimir_saida(hora_convertida, periodo)

    repetir = input("Deseja converter outra hora? (S/N): ").upper()

    if repetir != "S":
        print("Programa encerrado.")
        break