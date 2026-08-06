nome = input("digite seu nome: ")
idade = int(input("digite sua idade:"))
ano = str((2026 - idade) + 65)

if idade == 65:
    print(f"O trabalhador {nome} poderá se aposentar no ano de {ano}")

