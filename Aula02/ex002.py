'''Sabemos que num triângulo
retângulo, o quadrado da hipotenusa
(a) é igual a soma do quadrado dos
catetos (b e c). Faça um fluxograma
que receba o valor dos catetos,
calcule e mostre o valor da
hipotenusa.'''
from math import sqrt 
cat1 = int(input())
cat2 = int(input())
hip = sqrt((cat1**2) + (cat2**2))
print(f"o valor da hipotenusa é {hip}")