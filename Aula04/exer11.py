print("Algoritmo de conversão pés, polegadas, jardas e milhas")
print("======================================================")
pes = int(input("Entre com o valor em pés: "))
polegada = pes * 12
jarda = pes / 3
milhas = jarda / 1760 
print("======================================================")
print (f" A medida em Polegadas é : {polegada}")
print (f" A medida em Jardas é : {jarda:.2f}")
print (f" A medida em Milhas é : {milhas:.2f}")
