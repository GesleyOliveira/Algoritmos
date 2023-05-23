def totalpc(cabeca, pe):
    patos = ((4*cabeca) - pe)/6;
    coelhos = cabeca - (((4*cabeca) - pe)/6);
    return patos, coelhos

cabeca = int(input("Entre com as cabeças: "))
pe = int(input("Entre com os pés: "))

print(totalpc(cabeca, pe))

"""cabeca = pato + coelho 
coelho = cabeca - pato

pato = coelho - cabeca

pes = 2*pato + 4*coelho


pato = coelho - cabeca
coelho = cabeca - pato

coelho = cabeca - (((4*cabeca) - pe)/6)

pes = 2 * (coelho - cabeca) + 4 * coelho
pes = 2 * coelho - 2 * cabeca + 4 * coelho
pes = 6 * coelho - 2 * cabeca 
pes = 6 * (cabeca - pato) - 2 * cabeca
pes = 6 * cabeca - 6 * pato - 2 * cabeca
pes = 4 * cabeca - 6 * pato
6 * pato + pes = 4 cabeca
pato = ((4*cabeca) - pe)/6"""






