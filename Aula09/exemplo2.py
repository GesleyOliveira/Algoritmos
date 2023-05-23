lista = [0]*4
print(lista)

lista2 = [1, 1, 1]
print(lista2)


lista3 = lista + lista2
print(lista3)

lista3 = [0, 0, 0]
for i in range(0, 3):
    lista3[i] = lista[i] + lista2[i]
print(lista3)

lista[3] = 'a'
lista2.append('b')
print(lista[3]+lista2[3])

print(lista)
del lista[3]
print(lista)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[4:7])
print(lista[::-1])
print(lista[-2:-5:-1])

vetor = [0]*10
print(vetor)
vetor [0] = 3
print(vetor)

lista = [1, 30, 12, 4, -3, 'c']
print(lista)
print(len(lista))
del lista[5]
print(lista)
print(min(lista))
print(max(lista))
l = ['a', 'ab', 'bb', 'b', 'c']
print(min(l))
print(max(l))

# interável = uma string, uma lista etc

lista = list('batatinha quando nasce')
print(lista)
lista = ''.join(lista)
print(lista)

lista = list(range(1, 11))
print(lista)

a= list('texto')
b= list('text')
print(a==b)
print(a[0:4]==b[0:4])

print('t' in a)
print(a)
a[1] = 'amor'
print(a)
