from math import prod
lista = []
lista2 = []

n = str(input("Entre com um número positivo: "))
lista = list(n)

for i in lista:
    lista2 += [int(i)]

soma = sum(lista2)
multiplicacao = prod(lista2)

print(lista2)
print(soma)
print(multiplicacao)

    
