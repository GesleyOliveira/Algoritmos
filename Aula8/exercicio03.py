num = input("Digite nove caracteres numéricos: ")

if len(num) != 9 or not num.isdigit():
    print("O valor digitado não é válido.")
else:
    num_mil = int(num[0:1])
    num_cem = int(num[1:4])
    num_dez = int(num[4:7])
    num_un = int(num[7:9])
    
    print(f"{num_mil}.{num_cem}.{num_dez},{num_un}")
    

    
   