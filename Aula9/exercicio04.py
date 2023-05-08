lista = [0]*3
lista_inv = []
marcador = 0

for i in lista:
    lista = list(input(f"Entre com a {i+1} palavra: "))
    if len(lista) <= 3:
        break
for i in lista:
    lista_inv = lista.reverse()
    
print(lista_inv)