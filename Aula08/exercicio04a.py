frase = (input("Entre com uma frase: "))
qtd = 0
for letra in frase:
    if letra.lower() in 'aeiouáéíóúâêôàãõ':
        qtd += 1

print(f"Quantidade de vogais = {qtd}")


