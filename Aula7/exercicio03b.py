# Definindo as variáveis
soma_peso = 0
soma_altura = 0
maior_imc = 0
menor_imc = float('inf')  # atribuindo o maior valor possível para garantir que o primeiro valor lido seja menor

# Lendo o peso e a altura das 20 pessoas
for i in range(1, 6):
    print(f'Pessoa {i}')
    peso = float(input('Digite o peso em kg: '))
    altura = float(input('Digite a altura em metros: '))
    
    # Calculando o IMC
    imc = peso / altura ** 2
    
    # Atualizando as variáveis
    soma_peso += peso
    soma_altura += altura
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc: 
        menor_imc = imc

# Calculando as médias
media_peso = soma_peso / 5
media_altura = soma_altura / 5

# Exibindo os resultados
print(f'\nPeso médio: {media_peso:.2f} kg')
print(f'Altura média: {media_altura:.2f} m')
print(f'Maior IMC: {maior_imc:.2f}')
print(f'Menor IMC: {menor_imc:.2f}')
