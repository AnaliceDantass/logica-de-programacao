pontos = 0
questao = 1

while questao <= 10:
    resposta = input(f"resposta da questão %d: " % questao)
    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "d":
        pontos = pontos + 1
    questao +=1
print("o aluno fez %d ponto(s)"%pontos)

