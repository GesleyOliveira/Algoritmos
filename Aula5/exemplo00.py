ch = input("Digite a tecla p: ")
if (ch == "p"):
    print(f"Você pressionou a tecla p")
else:
    print(f"Você não digitou a tecla p, mas digitou a tecla: {ch}")


a = int(input("Entre com a: "))
b = int(input("Entre com b: "))
if (b):
    print(f"Divisão: {a/b}")
else:
    print("Não posso dividir por zero")