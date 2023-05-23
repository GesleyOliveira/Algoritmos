nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if (media <= 10.0) and (media >= 7.0):
    print("Aprovado")
elif (media >= 3.0) and (media < 7.0):
    print("Exame!")
    nota = 12 - media
    print(f"Você precisa tirar nota {nota} para ser aprovado")
elif (media >=0) and (media < 3.0):
    print("Reprovado")
else:
    print("Notas inválidas")