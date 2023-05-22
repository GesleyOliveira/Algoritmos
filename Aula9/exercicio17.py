def verificar_simetria(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# Função para criar uma matriz 8x8 a partir de uma lista de listas
def criar_matriz():
    matriz = []
    for i in range(8):
        linha = input(f"Digite os 8 valores da linha {i + 1}: ").split()
        linha = [int(num) for num in linha]
        matriz.append(linha)
    return matriz

# Criar a matriz
matriz = criar_matriz()

# Verificar simetria
simetrica = verificar_simetria(matriz)

# Exibir resultado
if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")
