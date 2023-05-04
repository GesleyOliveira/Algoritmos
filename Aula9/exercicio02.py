vetor = []

for i in range(1, 11):
    valor = int(input(f"Digite o {i}º valor: "))
    vetor.append(valor)

maior_valor = vetor[0]
posicao_maior_valor = 0

for i in range(1, 10):
    if vetor[i] > maior_valor:
        maior_valor = vetor[i]
        posicao_maior_valor = i

print("O maior valor é {maior_valor} e está na posição {posicao_maior_valor}")
