print("Algoritmo Hora para minutos")
print("===========================")
valor = float(input("Insira a hora: "))
hora = int(valor)
minutos = (valor - hora) * 100
minutos_totais = (hora * 60) + minutos
print("===========================")
print (f"Total em minutos: {minutos_totais}")

