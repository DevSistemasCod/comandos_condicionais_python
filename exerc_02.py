print("-- Identificar se número é Positivo ou Negativo --")
numero = int(input("Entre com um número: "))

if(numero > 0):
    print(f"O número {numero} é Positivo. ")
elif(numero < 0):
    print(f"O número {numero} é Negativo. ")
else:
    print(f"O número {numero} é Zero. ")