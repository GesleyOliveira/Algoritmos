dic = {}

for i in range(1,3):
    print("----------------------------")
    print(f"Pessoa {i}")
    nome = input(f"Entre com o nome: ")
    idade = input(f"Entre com a idade: ")
    dic[nome] = idade

soma = 0

for idade in dic.values():
    soma += idade
    media = soma / len(dic)
print(f"A amédia das idades é {media}")
    
for nome, idade in dic.items():
    if idade > media:
        print(f"{nome} tem {idade} anos!")