
soma_peso = 0
soma_altura = 0
marcador = 0
imc_maior = 0
imc_menor = float("inf")

while marcador < 20:
    marcador += 1
    peso = float(input(f"Entre com o peso da {marcador}ª pessoa: "))
    altura = float(input(f"Entre com a altura da {marcador}ª pessoa: "))
    imc = peso / (altura * altura)
    soma_peso += peso
    soma_altura += altura
    if imc > imc_maior:
        imc_maior = imc
    elif imc < imc_menor:
        imc_menor = imc
    
    
media_peso = soma_peso / marcador
media_altura = soma_altura / marcador
print(f"O peso médio das {marcador} pessoas é {media_peso:.2f}Kg, a altura média é {media_altura:.2f}m")
print(f"O maior IMC é {imc_maior:.2f} e o menor é {imc_menor:.2f}")