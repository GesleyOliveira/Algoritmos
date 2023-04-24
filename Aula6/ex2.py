valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 5000:
    desconto = valor_compra * 0.3
else:
    if valor_compra <= 1000:
        desconto = valor_compra * 0.1
    else:
        desconto = valor_compra * 0.2
novo_valor = valor_compra - desconto
print(f"Valor da Compra: {valor_compra:10.2f}")
print(f"Valor da Compra: {desconto:10.2f}")
print(f"novo_valor: {novo_valor:10.2f}")

