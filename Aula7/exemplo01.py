soma = 0
for x in range(1,11):
    idade = int(input(f"Digite a {x}a. idade: "))
    soma = soma + idade
media = soma / 10
print(f"A média das idades é igual a {media:.2f}")