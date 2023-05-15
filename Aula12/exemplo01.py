def desenha(n): # poderia ser def desenha(n=50), ai ele assumiria o valor de n como 50, se não fosse declarado posteriormente
    for i in range(0, n):
        print("-", end='')
    print() 

desenha(30)
print(f"** usando funções **")
desenha(40)   