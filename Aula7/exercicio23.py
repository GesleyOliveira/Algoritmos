soma = 0

while True:
    m = int(input("Digite o valor de m: "))
    n = int(input("Digite o valor de n: "))

    if m <= n:
        print("Erro: m deve ser maior do que n. Digite novamente.\n")
        continue

    for i in range(n, m+1):
        soma += i

    print("A soma de todos os números inteiros entre {} e {} é {}.\n".format(m, n, soma))

    resposta = input("Deseja digitar outro par de valores [m,n]? (S/N) ").upper()

    if resposta == "N":
        break

print("Programa encerrado.")

