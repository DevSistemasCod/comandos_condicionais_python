IDADE_MIN_HOMEM = 63
IDADE_MIN_MULHER = 58

TEMPO_SERV_HOMEM = 30
TEMPO_SERV_MULHER = 35

genero = input("Qual o seu gênero")

if(genero == "h"):
    idade = input("Informe a sua idade:")
    if(idade >= IDADE_MIN_HOMEM ):
        print("Pode Aposentar por idade")
    
    tempo_de_servico =  input("Informe o tempo de seriço:")
    if(tempo_de_servico >= TEMPO_SERV_HOMEM):
        print("Pode Aposentar por tempo de serviço")

elif(genero == "m"):
    idade = input("Informe a sua idade:")
    if(idade >= IDADE_MIN_MULHER ):
        print("Pode Aposentar por idade")
    
    tempo_de_servico =  input("Informe o tempo de seriço:")
    if(tempo_de_servico >= TEMPO_SERV_MULHER):
        print("Pode Aposentar por tempo de serviço")

else:
    print("As entradas aceitas são h ou m")