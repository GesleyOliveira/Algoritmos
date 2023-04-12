primeiro_nome = str(input("Digite o seu primeiro nome: "))
segundo_nome = str(input("Digite o seu segundo nome: "))
terceiro_nome = str(input("Digite o seu terceiro nome: "))
nome_completo= primeiro_nome +' '+ segundo_nome +' '+ terceiro_nome

print(f"Nome Completo: {nome_completo}!")

# Criptografia
# print(nome_completo[indice], "-" , chr(ord(nome_completo[indice])+1))

nome_cripto = ''
for indice in range(0, len(nome_completo)):
    nome_cripto += chr(ord(nome_completo[indice])+1)

print(f"Nome Cripto: {nome_cripto}")

