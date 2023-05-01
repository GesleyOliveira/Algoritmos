somap = 0
somaa = 0
maior_imc = 0
menor_imc = float("inf")

for i in range(1, 6):
    peso = float(input(f"Entre com o peso da {i}a pessoa: "))
    altura = float(input(f"Entre com a altura da {i}a pessoa: "))
    imc = (peso/(altura * altura))
    somap += peso
    somaa += altura
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
    pesot = somap / 5
    alturat = somaa / 5
    
print(f"O peso médio das 5 pessoas é: {pesot:.2f}Kg")
print(f"A altura média das 5 pessoas é: {alturat:.2f} metros")
print(f"O maior IMC é {maior_imc:.2f}")
print(f"O menor IMC é {menor_imc:.2f}")