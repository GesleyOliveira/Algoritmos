n = int(input("Entre com um número inteiro: "))
soma = 1

for i in range(n, 0, -1):
    soma *= i
print(f"O fatorial de {n}! é {soma}")