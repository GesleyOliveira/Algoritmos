pessoas = []

for i in range(1,6):
    print(f"Pessoa {i}: ")
    nome = input("Digite o nome: ")
    idade = int(input("Idade: "))
    calcado = int(input("Calçado: "))
    print("-----------------------------")
    pessoa = [nome, idade, calcado]
    pessoas.append(pessoa)

nova_lista = sorted(pessoas)

total_idades = 0
total_calcados = 0
print("Relação das pessoas e suas informações")
for i in range(0,5):
    total_idades += nova_lista[i][1]
    total_calcados += nova_lista[i][2]
    print(f"{nova_lista[i][0]} - {nova_lista[i][1]} - {nova_lista[i][2]}")
print("-----------------------------")
print(f"A média das idades: {total_idades/5}")
print(f"O número médio dos calçados: {int(total_calcados/5)}")
    