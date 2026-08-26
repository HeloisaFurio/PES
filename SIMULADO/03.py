valor_produto = (float(input("Insira o valor do produto: \n- ")))
quant_produto = (float(input("Quantos produtos você comprou? \n- ")))

total = valor_produto * quant_produto

if total >= 100:
    desconto = 0.1 * total
    total -= desconto

print (f"O total da sua compra foi de {total} reais")