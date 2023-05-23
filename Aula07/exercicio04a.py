soma = 0
contagem = 0

while True:
    numero = int(input("Digite um número par (ou 0 para sair): "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        soma += numero
        contagem += 1
    else:
        print("O número digitado não é par. Tente novamente.")

if contagem > 0:
    media = soma / contagem
    print("A média dos números pares digitados é:", media)
else:
    print("Nenhum número par foi digitado.")