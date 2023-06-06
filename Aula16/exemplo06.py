def entrada():
    try:
        num = int(input("Informe um número: "))
    except:
        return None
    else:
        return num
    finally:
        print("Fim do Bloco")

a = entrada()
print(a)