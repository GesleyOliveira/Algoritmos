l1 = []
l2 = []


for i in range(1,5):
    x = int(input(f"Entre com o {i} valor: "))
    l1.append(x)
print(f"L1 = {l1}")
for i in range(1,5):
    x = int(input(f"Entre com o {i} valor: "))
    l2.append(x)
print(f"L2 = {l2}")
# transforma as listas em conjuntos     
c1 = set(l1)
c2 = set(l2)
print(f"C1 = {c1}")
print(f"C2 = {c2}")
# une as duas listas
c = c1.union(c2) # se houvesse três conjuntos seria: c1.union(c2).union(c3)
# mostra o conjunto final
print(c)
