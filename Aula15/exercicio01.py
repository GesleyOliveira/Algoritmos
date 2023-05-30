arquivo = open("usuarios.txt", encoding="utf-8")
texto = arquivo.read()
texto = texto.split("\n")

soma = 0

for i in texto:
    valor = i.split(",")
    lista = int(valor[1])
    soma += lista

print("Nr.     Usuário     Espaço utilizado     % do uso")
numero = 0
total = 0
mb = 1048576
for i in texto:
    termo = i.split(",")
    nome = termo[0]
    valor = int(termo[1])
    numero += 1
    print(f"{numero}       {nome}       {valor/mb:.2f} MB   {((valor/soma)*100):.2f}%")

print(f"Espaço total ocupado: {soma/mb:.2f} MB")
print(f"Espaço médio ocupado: {(soma/mb)/numero:.2f} MB")

"""print("Nr.     Usuário     Espaço utilizado     % do uso")
numero = 0
total = 0
for i in texto:
    termo = i.split(",")
    nome = termo[0]
    valor = (int(termo[1])/1048576)
    numero += 1
    total += valor
    soma = valor/total
    print(f"{numero}       {nome}       {valor} MB   {soma} ")"""

