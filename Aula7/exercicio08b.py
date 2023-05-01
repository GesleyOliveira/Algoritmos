numero = int(input("Digite um número inteiro maior que 1: "))

divisores = 0

if numero <= 1:
    print("Entre com um número maior que 1!")
else:
    for i in range(2, numero):
        if numero % i == 0:
            divisores += 1
            break
    if divisores == 0:
        print("{} é um número primo.".format(numero))
    else:
        print("{} não é um número primo.".format(numero))