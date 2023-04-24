numero = int(input("Entre com um número: "))
soma = 0
resta = 0

while numero != 0:
    resta = numero % 10
    soma += resta
    numero = int(numero/10)
print(f"A soma dos digitos é {soma}")
