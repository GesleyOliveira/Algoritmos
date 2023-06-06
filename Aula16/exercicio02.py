arquivo = open("Aula16/carros.txt", encoding="utf-8")
texto = arquivo.read()
texto = texto.split("\n")
listacarros = texto

consumo = open("Aula16/consumo.txt", encoding="utf-8")
texto2 = consumo.read()
texto2 = texto2.split("\n")

carroconsumo = []

for i in texto:
    for j in 
    carroconsumo.append(texto2[i])

print(carroconsumo)

