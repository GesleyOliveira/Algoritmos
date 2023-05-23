soma = 0
marcador = 0

while True:
    idade = int(input("Entre com a idade em anos: "))
    if idade == 0:
        break
    soma += idade
    marcador += 1
    
if marcador > 0:
    media = soma / marcador
print(f"A idade média dos individuos é de {media} anos, e o número total é de {marcador} individuos")