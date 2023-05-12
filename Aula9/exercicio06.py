from random import randint

dado1 = [0]*7
dado2 = [0]*7
est = [0]*7
soma = 0

for i in range(30000):
    x = randint(1, 6)
    dado1[x] = dado1[x] + 1
    y = randint(1, 6)
    dado2[y] = dado2[y] + 1
    soma = dado1[x] + dado2[y]

for i in range(1, 7):
    est[i] = dado1[i]/30000
    est[i] = dado2[i]/30000
for i in range(1, 7):
    print(f'Lado {i} foi sorteado {dado1[i]} = {est[i]:.2%}')
    print(f'Lado {i} foi sorteado {dado2[i]} = {est[i]:.2%}')


