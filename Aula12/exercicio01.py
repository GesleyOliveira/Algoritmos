def epar(x):
    return (x % 2 == 0)

n = int(input("Entre com um valor: "))
if epar(n):
    print(f"O número {n} é par!")
else:
    print(f"O número {n} é ímpar!")
