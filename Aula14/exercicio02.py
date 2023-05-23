def primo(n):
    i = 1
    soma = 0
    if n == 1 or n == 0:
        return False
    while i <= n:
        if (n % i) == 0:
            soma += 1
        i += 1
    if soma == 2:
        return True
    else:
        return False
    
"""n = int(input("Entre com um número: "))
print(primo(n))"""

def qtd_primo(n):
    lista = []
    qtd = 0
    for i in range(0, n+1):
        if primo(i):
            lista.append(i)
    qtd = len(lista)
    return qtd

def soma_primo(n):
    lista = []
    soma = 0
    for i in range(0, n+1):
        if primo(i):
            lista.append(i)
    soma = sum(lista)
    return soma

n = int(input("Entre com um número: "))


for i in range(0, n):
    if primo(i):
        print(i)

print(f"A quantidade de número primo é: {qtd_primo(n)}")
print(f"A soma dos números primos é: {soma_primo(n)}")


