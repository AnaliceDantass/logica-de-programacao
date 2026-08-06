nota1 = float(input("insira sua nota parcial: "))
nota2 = float(input("insira sua nota final: "))

media = (nota1 + nota2) / 2

if media == 10 and media >= 9:
    aproveitamento = "A"
    print("Aluno aprovado com nota A")
elif media < 9 and media >= 7.5:
    aproveitamento = "B"
    print("Aluno aprovado com nota B")
elif media < 7.5 and media >= 6:
    aproveitamento = "C"
    print("Aluno aprovado com nota C")
elif media < 6 and media >=4:
    aproveitamento = "D"
    print("Aluno reprovado com nota D")
elif media < 4:
    aproveitamento = "E"
    print("Aluno reprovado com nota E")

print(f"As notas parciais do aluno foram: {nota1} e {nota2}. Sua média foi {media}, e o seu aproveitamento foi {aproveitamento} com média {media}.")


