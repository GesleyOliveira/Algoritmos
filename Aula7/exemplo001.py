"""Faça um algoritmo que leia um valor N inteiro
e positivo, calcule e mostre o valor E,
conforme a fórmula a seguir..
"""
numero = int(input("Entre com um valor inteiro e positivo: "))
e = 0

for i in range(1, numero+1):
    e += (2**i) 
print(f"O valor de E é {e}")