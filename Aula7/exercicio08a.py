n = int(input("Entre com um número inteiro maior que 1: "))


if n <= 1:
    print("Entre com um valor maior que 1")
elif n == 2 or n ==3 or n ==5 or n ==7:
    print(f"O número {n} é primo!")
elif n % 2 == 0:
    print(f"O número {n} não é primo!")
elif (n%3==0) or (n%5==0) or (n%7==0):
    print(f"O número {n} não é primo!")
else:
    print(f"O número {n} é primo!")
    

