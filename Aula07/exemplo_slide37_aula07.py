"""Elaborar um algoritmo que imprime na tela os
dez primeiros múltiplos de um número
inteiro qualquer fornecido pelo usuário (lido).
No final, imprima também a soma destes dez
números.
Exemplo da saída:
Valor lido: 3
Lista de Múltiplos: 3 6 9 12 15 18 21 24 27 30
Soma = 165 """

n = int(input("Entre com um número inteiro: "))
multiplos = []
soma = 0
i = 1

while i <= 10:
    multi = n * i
    multiplos.append(multi)
    soma += multi
    i += 1
print(f"O valor lido é: {n}")
print("Lista de Múltiplos:", " ".join(map(str, multiplos)))
print(f"A soma = {soma}")