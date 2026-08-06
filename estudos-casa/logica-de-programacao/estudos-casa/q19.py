montante = 0
objetivo = 10000
capital = 200
txJuros = .3/100
meses = 0 # nao sei quantos meses vai demorar para chegar esse valor

while montante < objetivo:
    montante += capital #a plicação no início do período 
    juro = montante * txJuros # juros compostos
    montante += juro
    meses += 1
    print(f"montante no mês {meses} = R$ {montante:.2f}")

print(f"número de meses: {meses}")