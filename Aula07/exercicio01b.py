n = int(input("Entre com um valor inteiro e positivo: "))
e = 0
for i in range(1, n+1, 1):
    e += 2**i
print(f"O valor da fórmula E é {e}")