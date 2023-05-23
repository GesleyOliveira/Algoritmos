ano = int(input("Entre com o ano de nascimento: "))
anoatual = int(input("Entre com o ano atual: "))
idade = anoatual - ano
if (idade >= 16) and (idade >= 18):
    print(f"Você tem {idade} anos, tem idade para dirigir e votar!")
elif (idade >= 16):
    print(f"Você tem {idade} anos, tem idade para votar!")
else: 
    print(f"Você tem {idade} anos, não tem idade para dirigir e nem para votar!")