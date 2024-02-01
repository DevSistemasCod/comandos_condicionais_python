print("-- Identificar se número é Par ou Ímpar --")
numero = int(input("Entre com um número: "))

resto_divisao = numero % 2

if(resto_divisao == 0):
    print(f"O número {numero} é par. ")
else:
    print(f"O número {numero} é ímpar. ")