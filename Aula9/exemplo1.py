mat_notas = []
notas = []
vet_nomes_al = []
ind_lin, ind_col = 0, 0
for ind_lin in range(0, 5):
    nome = input("Nome do Aluno: ")
    vet_nomes_al.append(nome)
for ind_col in range(0, 3):
    if ind_col != 2:
        nota = float(input(f'Digite a nota Bim {ind_col+1}: '))
        notas.append(nota)
else:
    nota = float(input('Digite a Média Final : '))
    notas.append(nota)
    mat_notas.append(notas)