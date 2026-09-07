def retangulo(base, altura):
    if base < 1:
        base = 1
    elif base > 20:
        base = 20
    if altura < 1:
        altura = 1
    elif altura > 20:
        altura = 20
    
    if altura == 1:
        desenho = ("+" + "-" * base + "+")
    else:
        desenho =("+" + "-" * base + "+")

        for i in range(altura - 2):
            desenho += ("\n|" + " " * base + "|")

        desenho += ("\n+" + "-" * base + "+")
        
        return(desenho)
    
base = int(input("Digite a base do retângulo (1 a 20): "))
altura = int(input("Digite a altura do retângulo (1 a 20): "))
print(retangulo(base, altura))