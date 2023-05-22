def calcular_media_linhas_pares(matriz):
    soma = 0
    count = 0
    for i in range(len(matriz)):
        if i % 2 == 1:  
            for j in range(len(matriz[i])):
                soma += matriz[i][j]
                count += 1
    if count == 0:
        return 0
    else:
        return soma / count

def criar_matriz():
    matriz = []
    for i in range(5):
        linha = input(f"Digite os 5 valores da linha {i + 1}: ").split()
        linha = [float(num) for num in linha]
        matriz.append(linha)
    return matriz


matriz = criar_matriz()

media = calcular_media_linhas_pares(matriz)

print("A média dos elementos nas linhas pares da matriz é:", media)
