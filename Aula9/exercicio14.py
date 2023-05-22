matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input(f"Digite o elemento ({i+1}, {j+1}): "))
        linha.append(elemento)
    matriz.append(linha)

matriz_transposta = []
for i in range(3):
    linha_transposta = []
    for j in range(3):
        linha_transposta.append(matriz[j][i])
    matriz_transposta.append(linha_transposta)

print("Matriz transposta:")
for linha in matriz_transposta:
    print(linha)
