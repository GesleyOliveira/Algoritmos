altura = float(input("Entre com a sua altura: "))
genero = str(input("Entre com o seu sexo (M/F): "))
genero = genero.upper()

homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

if (genero == "M"):
    print(f"Seu peso ideal é {homem:.1f}Kg")
else:
    print(f"Seu peso ideal é {mulher:.1f}Kg")
    