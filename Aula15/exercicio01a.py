arquivoEntrada = open("usuarios.txt", encoding="utf-8")

linhas = arquivoEntrada.readlines()


usuarios = []
espacos_utilizados = []
espaco_total = 0.0
for linha in linhas:
    campos = linha.spli()
    usuario = campos[0]
    espacos_utilizados = int(campos[1])
    usuario.append(usuario)
    espacos_utilizados.append()