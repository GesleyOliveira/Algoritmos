num1 = int(input('Entre com o primeiro número: '))
num2 = int(input('Entre com o segundo número: '))
escolha = int(input("Escolha um número (1. Média, 2. Diferença, 3. Produto, 4. Divisão): "))

if escolha == 1:
    media = (num1 + num2) / 2
    print(f"A média entre {num1} e {num1} é {media}")
elif escolha == 2:
    if (num1 > num2):
        dif1 = num1 - num2
        print(f"A diferença entre {num1} - {num2} é {dif1}")
    else:
        dif2 = num2 - num1
        print(f"A diferença entre {num2} - {num1} é {dif2}")
elif escolha == 3:
    produto = num1 * num2
    print(f"O produto entre {num1} e {num2} é {produto}")
elif escolha == 4:
    if num2 == 0:
        print(f"{num2} incorreto! Insira um valor de {num2} maior que 0!" )
    else:
        divisao = num1 / num2
        print(f"A divisão entre {num1} e {num2} é {divisao}")
else:
    if escolha != (1 or 2 or 3 or 4):
        print(f"O valor de {escolha} está incorreto! Escolha valores entre 1 e 4")
    
    
    