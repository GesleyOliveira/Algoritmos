numero = float(input("Entre com um número: "))

if (numero >= 0):
    if (numero % 2 == 0):
        print(f"O número {numero} é positivo e par!")
    else: 
        print(f"O número {numero} é positivo e ímpar!")
else:
    if (numero % 2 == 0):
        print(f"O número {numero} é negativo e par!")
    else: 
        print(f"O número {numero} é negativo e ímpar!")