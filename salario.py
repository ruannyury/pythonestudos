# Escrever um programa de pagamento, para pagar ao funcionário
# 1.5 vezes o valor da taxa horária de pagamento pelo tempo
# trabalhado acima de 40 horas.

horas = input('Digite as horas trabalhadas:\n')
horas = int(horas)

taxa = input('Digite a taxa por hora:\n')
taxa = int(taxa)

if horas <= 40:
    pagamento = horas * taxa
else:
    pagamento = (taxa * 1.5) * horas

print('Pagamento: ', pagamento)
