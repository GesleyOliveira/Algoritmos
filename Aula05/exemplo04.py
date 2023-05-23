n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1+n2+n3)/3
if media >=7:
    print(f"Sua média é {media:.1f}. Aprovado!")
else:
    if media >= 3:
        print(f"Sua média é {media:.1f}. Exame!")
        nota = 12 - media
        print(f"Você precisa tirar no mínimo nota: {nota:.1f}")
    else: 
        print(f"Sua média é {media:.1f}. Reprovado!")

