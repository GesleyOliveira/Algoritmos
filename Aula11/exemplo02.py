palavras = []
lista = []

while True:
    palavra = input("Entre com uma palavra: ")
    if palavra != '':
        palavras.append(palavra)
    else:
        break
for palavra in palavras:
    lista.append(list(set(palavra)))
    
for item in lista:
    print(item)