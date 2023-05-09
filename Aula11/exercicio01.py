t = ()
for i in range(1, 6):
    x = int(input(f"Digite o {i}º numero: "))
    t = t + (x,) #ou poderia ser t = t + tuple([x])
    
print(t[::-1])
print(type(t))
