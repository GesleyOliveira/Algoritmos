pessoas = []

for i in range(1,6):
    print(f"pessoa {i}:")
    nome = input(f"Nome: ")
    idade = int(input("Idade: "))
    calcado = int(input("Calçado: "))
    pessoa = [nome, idade, calcado]
    pessoas.append(pessoa)
    
nova_lista = sorted(pessoas)
total_idade = 0
total_calcado = 0

print("Relação das pessoas e suas informações: ")
for i in range(1,6):
    total_idade += nova_lista[i][1]
    total_calcado += nova_lista[i][2]
    print(f"nova_lista[i][1]")