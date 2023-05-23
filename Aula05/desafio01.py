numero = int(input("Entre com um número inteiro, positivo e maior que zero: "))


if ((numero % 2) == 0) and (numero > 0):
    print(f"O número {numero} é par!")
elif numero > 0:
    print(f"O número {numero} é ímpar!")
else:
    if numero < 0:
        print(f"O número {numero} é menor que zero!")
