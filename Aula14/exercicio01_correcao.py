'''
cabeca = p + c => patos = cabeca - coelho
pes = 2 patos + 4 coeslho => pes = 2(cabeca - coelho) + 4 coelho 

pes = 2(cabeca - coelho) + 4 coelho
pes = 2 cabeca - 2 coelho + 4 coelho
pes 2 cabeca + 2 coelho

coelho = (pes - 2*cabeca) / 2

patos = cabeca - ((pes - 2*cabeca) / 2)

'''
def totalpc(cabeca, pe):
    patos = cabeca - ((pe - 2*cabeca) / 2);
    coelhos = (pe - 2*cabeca) / 2;
    return patos, coelhos

cabeca = int(input("Entre com as cabeças: "))
pe = int(input("Entre com os pés: "))

print(totalpc(cabeca, pe))