def numero_por_extenso(numero):
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco",
                "seis", "sete", "oito", "nove"]

    especiais = ["dez", "onze", "doze", "treze", "quatorze",
                 "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

    dezenas = ["", "", "vinte", "trinta", "quarenta",
               "cinquenta", "sessenta", "setenta",
               "oitenta", "noventa"]

    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos",
                "quinhentos", "seiscentos", "setecentos",
                "oitocentos", "novecentos"]

    if numero == 0:
        return "zero"

    if numero == 100:
        return "cem"

    texto = ""

    if numero >= 1000:
        milhar = numero // 1000
        if milhar == 1:
            texto += "mil"
        else:
            texto += unidades[milhar] + " mil"

        numero %= 1000
        if numero > 0:
            texto += " "

    if numero >= 100:
        centena = numero // 100
        texto += centenas[centena]
        numero %= 100
        if numero > 0:
            texto += " e "

    if numero >= 20:
        dezena = numero // 10
        texto += dezenas[dezena]
        numero %= 10
        if numero > 0:
            texto += " e "

    elif numero >= 10:
        texto += especiais[numero - 10]
        numero = 0

    if 0 < numero < 10:
        texto += unidades[numero]

    return texto


def valor_por_extenso(valor):
    reais = int(valor)
    centavos = round((valor - reais) * 100)

    if reais == 1:
        texto_reais = "um real"
    else:
        texto_reais = numero_por_extenso(reais) + " reais"

    if centavos == 0:
        return texto_reais
    elif centavos == 1:
        return texto_reais + " e um centavo"
    else:
        return texto_reais + " e " + numero_por_extenso(centavos) + " centavos"


valor = float(input("Digite um valor em reais: "))
print(valor_por_extenso(valor))