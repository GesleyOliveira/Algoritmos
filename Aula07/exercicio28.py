numero = 0
div = 0

while True:
    n = int(input("Entre com um número inteiro maior que 1: "))
    if n > 1:
        break
    print("Entre com um número maior que 1!")
for i in range(2, n):
    if n % i == 0:
        div += 1
        break
if div == 0:
    print(f"O número {n} é primo")
else:
    print(f"O número {n} não é primo")