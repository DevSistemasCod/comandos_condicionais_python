prmeira_nota = float(input("Informe a Primeira Nota: "))
segunda_nota = float(input("Informe a Segunda Nota: "))

media_notas = (prmeira_nota + segunda_nota)/2

if(media_notas > 5):
    print(f"O aluno passou com média {media_notas}")
elif(media_notas < 5) and (media_notas > 3):
    print(f"O aluno está de recuperação média atual: {media_notas}")
else:
    print(f"Aluno reprovado com média: {media_notas}")