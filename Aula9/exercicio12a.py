def multiplicar_matriz_por_maior_elemento(matriz):
    maior_elemento = matriz[0][0]  # Assume o primeiro elemento como o maior inicialmente

    # Encontra o maior elemento na matriz
    for linha in matriz:
        for elemento in linha:
            if elemento > maior_elemento:
                maior_elemento = elemento

    # Multiplica a matriz pelo maior elemento
    matriz_resultante = [[elemento * maior_elemento for elemento in linha] for linha in matriz]
    return matriz_resultante


# Função para ler uma matriz 2x2 do usuário
def ler_matriz():
    matriz = []
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = int(input(f"Digite o elemento ({i+1}, {j+1}): "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


# Leitura da matriz digitada pelo usuário
print("Digite os elementos da matriz 2x2:")
matriz_digitada = ler_matriz()

# Multiplica a matriz pelo maior elemento
matriz_resultante = multiplicar_matriz_por_maior_elemento(matriz_digitada)

# Exibe a matriz resultante
print("Matriz resultante:")
for linha in matriz_resultante:
    print(linha)

