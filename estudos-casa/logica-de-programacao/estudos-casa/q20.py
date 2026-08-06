numero1 = int(input("digite o primeiro número: "))
numero2 = int(input("digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 /numero2

print("qual operação você deseja realizar? ")
print(" 1 - soma \n 2- subtração \n 3 - multiplicação \n 4 - divisão")
opcao = int(input("digite a opção que deseja:"))

if opcao == 1:
    print(f"a soma  dos números é igual a {soma}")
elif opcao == 2:
    print(f"a subtração dos números é igual a {subtracao}")
elif opcao == 3:
    print(f"a multiplicação dos números é igual a {multiplicacao}")
elif opcao == 4:
    print(f"a divisão dos números é igual a {divisao}")
