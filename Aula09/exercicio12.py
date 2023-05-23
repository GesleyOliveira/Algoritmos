matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o elemento ({i+1}, {j+1}): "))
        linha.append(elemento)
    matriz.append(linha)

maior_elemento = matriz[0][0]

for linha in matriz:
    for elemento in linha:
        if elemento > maior_elemento:
            maior_elemento = elemento
            
nova_matriz = []

for linha in matriz:
    nova_linha = []
    for elemento in linha:
        nova_linha.append(elemento * maior_elemento)
    nova_matriz.append(nova_linha)
    
print("Nova matriz")
print(f"1,1 = {nova_matriz[0][0]}")
print(f"1,2 = {nova_matriz[0][1]}")  
print(f"2,1 = {nova_matriz[1][0]}")     
print(f"2,2 = {nova_matriz[1][1]}") 