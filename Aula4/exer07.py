valor = float(input("Entre com o valor de depósito: "))
taxaJuros = float(input("Entre com a taxa de juros: "))
rendimento = valor * (taxaJuros/100)
total = rendimento + valor
print(f'Seu rendimento será de {rendimento}, e o valor total será de {total}')