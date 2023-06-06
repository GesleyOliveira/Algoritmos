try:
    num = int(input("Informe um número: "))
except:
    print("Valor incorreto!")
else:
    print(f"Você digitou {num}")
finally:
    print("Fim do Bloco")
