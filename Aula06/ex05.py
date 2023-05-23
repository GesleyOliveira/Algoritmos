tipo = str(input("Entre com tipo de combustível (a, d ou g): "))
volume = float(input("Entre com o volume: "))
tipo = tipo.lower()

if tipo == "a":
    a = volume * 1.7997
    print(f"O valor a ser pago pelo volume de {volume} de álcool será: R${a:.2f}")
elif tipo == "d":
    d = volume * 0.9798
    print(f"O valor a ser pago pelo volume de {volume} de diesel será: R${d:.2f}")
elif tipo == "g":
    g = volume * 2.1009
    print(f"O valor a ser pago pelo volume de {volume} de gasolina será: R${g:.2f}")
else:
    print(f"O tipo {tipo} é inválido! Entre com os tipo a, d ou g!")