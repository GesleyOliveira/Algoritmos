idade = int(input("Entre com a idade do nadador: "))

if (5 <= idade <= 7):
    print(f"A categoria do nadador com base na idade de {idade} anos é infantil!")
elif (8 <= idade <= 10):
    print(f"A categoria do nadador com base na idade de {idade} anos é juvenil!")
elif (11 <= idade <= 15):
    print(f"A categoria do nadador com base na idade de {idade} anos é adolescente!")
elif (16 <= idade <= 30):
    print(f"A categoria do nadador com base na idade de {idade} anos é adulto!")
elif ( idade >= 30):
    print(f"A categoria do nadador com base na idade de {idade} anos é sênior!")
else:
    print(f"A idade {idade} anos está fora de uma categoria!")