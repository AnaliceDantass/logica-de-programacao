nota1 = float(input("insira a sua primeira nota parcial: "))
nota2 = float(input("insira a sua segunda nota parcial: "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("parabéns, você foi aprovado")
elif media < 7:
    print("reprovado.")
elif media == 10:
    print("você foi aprovado com distinção, parabéns")

