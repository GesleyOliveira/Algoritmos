idades = {
    'ana': 34,
    'pedro': 31,
    'jose': 45,
    'joão': 18
}
soma = 0

for idade in idades.values():
    print(f"A idade que está sendo somanda agora é {idade}")
    soma += idade
media = soma / len(idades)
print(f"A média das idades é {media}")