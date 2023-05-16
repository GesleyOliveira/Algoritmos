def ano_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return 1
    else:
        return 0

ano = int(input("Entre com um ano: "))
resultado = ano_bissexto(ano)
print(resultado)  # Isso imprimirá 1, indicando que 2024 é um ano bissexto
