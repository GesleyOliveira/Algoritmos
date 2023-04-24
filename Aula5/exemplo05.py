print("Método de peso ideal!")
sexo = input("Entre com o seu sexo (M) ou (H): ")
altura = float(input("Entre com sua altura em metros: "))
if sexo.upper() == "M":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7
print(f"Seu peso ideal é {peso:.1f} kg.")


