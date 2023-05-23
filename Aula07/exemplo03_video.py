numero = int(input("Entre com um número: "))
fatorial = 1

if numero < 0:
    print(f"Não existe fatorial de número negativo, valor {numero} incorreto!")
elif numero == 0:
    print(f"fatorial de {numero} é 1!")
else:
    for i in range(1, numero+1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")