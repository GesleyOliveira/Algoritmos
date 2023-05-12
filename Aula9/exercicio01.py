vetor = []
for i in range(11):
    x = int(input(f"Digite o {i+1}o. valor: "))
    vetor.append(x)
print(vetor[::-1])
#ou
vetor.reverse()
print(vetor)