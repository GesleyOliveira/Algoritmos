a = {1,2,3}
b = {1,2,6,7}
c = a.union(b) #União entre 'a' e 'b' exclusos os elementos iguais
d = set([1,5,6,7,3,2,1,5]) #set é uma função que cria um conjunto a partir de uma interável
6 in d # Retorna True, pois tem o elemento '6' no set 'd'
9 in d # Retorna False, pois não tem o elemento '9' no set 'd'
d.add(6) #não adiciona, pois já há o elemento '6' no set 'd'
d.add(0) #adiciona elementos
e = {1, 'Gesley', 3.5, 'helloworld', (1,2)}
t = (1, 'Gesley', 3.5, 'helloworld', [1,2])
f = a.intersection(b) #elementos em comum, intersecção 
a.difference(b)
b.difference(a)

