print("Algoritmo Quilowatts consumido por uma residência")
print("=================================================")
quilowatt = 1302/8
consumo = int(input("Insira o consumo: "))
Reais = consumo * quilowatt
Desconto = Reais * 0.85
print("=================================================")
print (f" O valor de cada Quilowatt é: {quilowatt:.2f} Reais")
print (f" O valor a ser pago é: {Reais:.2f}")
print (f" O valor a ser pago com desconto de 15% é: {Desconto:.2f}")
