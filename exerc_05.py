lado1 = int(input("Informe o primeiro lado: "))
lado2 = int(input("Informe o segundo lado: "))
lado3 = int(input("Informe o terceiro lado: "))

# Validação 1 - Condição de Existência 
if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado2 + lado3) > lado1):
    
    if(lado1 == lado2 == lado3):
        print("Triângulo equilátero")
    elif((lado1 == lado2) or  (lado1 == lado3) or (lado3 == lado2)):
        print("Triângulo isóceles")
    else:
        print("Triângulo escaleno")
else:
    print("Condição de Existência para ser um triângulo inválida !!!")