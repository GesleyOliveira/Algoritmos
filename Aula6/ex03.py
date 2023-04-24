valor = float(input("Entre com o valor da compra: "))
desconto_trinta = valor * 0.7
desconto_vinte = valor * 0.8
desconto_dez = valor * 0.9

if valor > 5000: 
    print(f"A compra no valor de R${valor} receberá desconto de 30%, ficando em {desconto_trinta:.2f} ")
elif valor >= 1001:
    print(f"A compra no valor de R${valor} receberá desconto de 20%, ficando em {desconto_vinte:.2f} ")
else:
    print(f"A compra no valor de R${valor} receberá desconto de 10%, ficando em {desconto_dez:.2f} ")