import math
e = 0
n = int(input("Digite um número inteiro positivo: "))
for i in range(n):
    e = e + math.pow(2, i+1)
print(f"O valor de E= {e:.2f}")