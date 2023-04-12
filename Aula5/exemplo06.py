print("Determinação do tipo de triângulo")
a = float(input("Entre com o lado 'A' do triângulo: "))
b = float(input("Entre com o lado 'B' do triângulo: "))
c = float(input("Entre com o lado 'C' do triângulo: "))  
if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Os lados formam um Triangulo!")
    if ((a==b) and (b==c)):
        print("Triângulo Equilátero!")
    elif (a == b) or (b == c) or (a == c):
        print("Triângulo Isósceles!")
    else:
        print("Triângulo Escaleno!")
else:
    print("Os lados informados não formam um triângulo!")


     