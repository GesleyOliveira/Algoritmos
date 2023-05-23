lista = []
contagem = 0

while True:
    n = int(input("Insira um valor par ou 0 para sair: "))
    if n == 0:
        break
    elif n % 2 == 0:
        lista.append(n)
        contagem += 1
    else:
        print(f"Valor {n} ímpar! Insira um valor par")
media = sum(lista) / contagem
print(f"A média dos números pares é {media}")