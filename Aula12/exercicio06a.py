def segundos(numero):
    valor = (numero).split(":")
    hora = int(valor[0]) * 3600;
    minuto = int(valor[1]) * 60;
    segundo = int(valor[2]);
    return(hora + minuto + segundo) 

numero = input("Entre com as horas:minutos:segundos: ")
print(segundos(numero))