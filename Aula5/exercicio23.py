preco = float(input("Entre com o preço líquido do produto: "))
codigo = int(input("Entre com o código de origem (1, 2, 3, 4 ou 5): "))


if codigo == 1:
    cod1 = preco * 1.11
    print(f"A procedencia do produto é sul, e o preço com imposto de 11% é {cod1}")
elif codigo == 2:
    cod2 = preco * 1.13
    print(f"A procedencia do produto é norte, e o preço com imposto de 13% é {cod2}")
elif codigo == 3:
    cod3 = preco * 1.09
    print(f"A procedencia do produto é nordeste, e o preço com imposto de 9% é {cod3}")
elif codigo == 4:
    cod4 = preco * 1.12
    print(f"A procedencia do produto é centro-oeste, e o preço com imposto de 12% é {cod4}")
elif codigo == 5:
    cod5 = preco * 1.18
    print(f"A procedencia do produto é sudeste, e o preço com imposto de 18% é {cod5}")
else:
    print(f"Valor de código {codigo} incorreto! Entre com um valor correto!")