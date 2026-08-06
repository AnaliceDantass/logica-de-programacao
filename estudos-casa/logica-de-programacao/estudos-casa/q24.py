numero = int(input("escolha um número de 1 a 10: "))
cont = 1

if numero >= 1 and numero <= 10:

    while cont <= 10:
        tabuada = numero * cont
        print ("%d X %d = %d" % (numero, cont, tabuada))
        cont = cont + 1

else:
    print("apenas valores de 1 a 10!")