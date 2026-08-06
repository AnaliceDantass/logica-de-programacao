numero = int(input("digite um número qualquer: "))

if numero % 3 == 0:
    print(f"o número {numero} é múltiplo de 3")
elif numero % 5 == 0:
    print(f"o número {numero} é múltiplo de 5")
elif numero % 3 == 0 and numero % 5 == 0:
    print(f"o número {numero} é múltiplo de 3 e de 5")
else:
    print(f"o número {numero} não é múltiplo de 3 e nem de 5")