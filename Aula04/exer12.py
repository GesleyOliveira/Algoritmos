degrau = float(input('Entre com a altura do degrau em cm: '))
escada = float(input('Entre com a altura desejável em m: '))
conv = escada * 100
div = int(conv / degrau) 
print(f'Para alcançar a altura de {escada}m, deverá subir {div:.2f} degraus')