from math import pow, pi
print("Calculo da área de um círculo")
print("==============================")
raio = float(input("Raio do círculo: "))
print("==============================")
area = pi * pow(raio, 2)
print (f"A área do círculo é: {area:5.3f} cm2")
