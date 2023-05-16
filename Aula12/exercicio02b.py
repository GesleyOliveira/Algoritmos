def eprimo(n):
    contador = 0
    for i in range(1, n+1):
        if(n % i) == 0:
            contador += 1
        i += 1
    if contador == 2:
        return True
    else:
        return False

x = int(input("Entre com um valor: "))
if eprimo(x):
    print(f"O número {x} é primo!")
else:
    print(f"O número {x} não é primo!")
