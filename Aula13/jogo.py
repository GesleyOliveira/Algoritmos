from funcoes import rola_dado
from time import sleep

print("----------------------------")
print("       Jogue o dado        ")
print("----------------------------")



while True:
    escolha = input("Digite <Enter> para rolar o seu dado: ")
    usuario = rola_dado()
    print("Agora é minha vez de jogar ...")
    for s in range(0,3):
        for i in range(0,3):
            print(".", end='\r')
            sleep(0.5)
            print("..", end='\r')
            sleep(0.5)
            print("...", end='\r')
            sleep(0.5)
    
    for _ in range(1, 1000000): # _ serve quando não se usa a variável
        pass
    computador = rola_dado()
    print(f"Você: {usuario} - Eu: {computador}")
    if usuario > computador:
        print("Você ganhou!!")
    elif computador == usuario:
        print("Empatamos!!")
    else:
        print("Eu ganhei!!")
    opcao = input("Você gostaria de jogar novamente? (S/N): ")
    if opcao.upper() == "N":
        break
print("Obrigado por Jogar! Agora vá estudar!!!")