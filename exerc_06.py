IDADE_MIN_HOMEM = 63
IDADE_MIN_MULHER = 58

TEMPO_SERV_HOMEM = 30
TEMPO_SERV_MULHER = 35

genero = input("Qual o seu gênero: ").lower()
genero 

if(genero == "h"):
    idade = int(input("Informe a sua idade: "))
    if(idade >= IDADE_MIN_HOMEM ):
        print("Pode se aposentar por idade")
    else:
        print("Não pode se aposentar por idade")

    tempo_de_servico =  int(input("Informe o tempo de serviço: "))
    if(tempo_de_servico >= TEMPO_SERV_HOMEM):
        print("Pode se aposentar por tempo de serviço")
    else:
        print("Não pode se aposentar por tempo de serviço")


elif(genero == "m"):
    idade = int(input("Informe a sua idade: "))
    if(idade >= IDADE_MIN_MULHER ):
        print("Pode se aposentar por idade")
    else:
        print("Não pode se aposentar por idade")

    tempo_de_servico =  int(input("Informe o tempo de serviço: "))
    if(tempo_de_servico >= TEMPO_SERV_MULHER):
        print("Pode se aposentar por tempo de serviço")
    else:
        print("Não pode se aposentar por tempo de serviço")


else:
    print("As entradas aceitas são h ou m")