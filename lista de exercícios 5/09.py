def numero_por_extenso(numero):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis",
                "sete", "oito", "nove"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze",
                 "quinze", "dezesseis", "dezessete",
                 "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta",
               "cinquenta", "sessenta", "setenta",
               "oitenta", "noventa"]

    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return especiais[numero - 10]
    else:
        dezena = numero // 10
        unidade = numero % 10

        if unidade == 0:
            return dezenas[dezena]
        else:
            return dezenas[dezena] + " e " + unidades[unidade]


def data_por_extenso(data):
    dia, mes, ano = data.split("/")

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    meses = [
        "janeiro", "fevereiro", "março", "abril",
        "maio", "junho", "julho", "agosto",
        "setembro", "outubro", "novembro", "dezembro"
    ]

    if ano == 2000:
        ano_extenso = "dois mil"
    elif ano == 2100:
        ano_extenso = "dois mil e cem"
    else:
        ano_extenso = "dois mil e " + numero_por_extenso(ano - 2000)

    return numero_por_extenso(dia) + " de " + meses[mes - 1] + " de " + ano_extenso


data = input("Digite uma data (DD/MM/AAAA): ")
print(data_por_extenso(data))
