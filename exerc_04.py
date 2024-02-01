numero1 = int(input("informe o primeiro número: "))
numero2 = int(input("informe o segundo número: "))

if(numero1 == numero2):
    print("Os números são iguais: ")
elif(numero1 > numero2):
    print(f"O número {numero1} é maior do que o número {numero2} ")
else:
    print(f"O número {numero2} é maior do que o número {numero1} ")

resultado = (numero1 + numero2)*2

if(resultado > 10):
    print(f"{resultado} é maior do que 10 ")
elif(resultado < 10):
    print(f"{resultado} é menor do que 10 ")
else:
    print(f"{resultado} é igual a 10 ")