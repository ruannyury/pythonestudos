#Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, 
#determinar quantos números da sequência são pares e quantos são ímpares
def main():
    try:
        somaPar = 0
        somaImpar = 0
        num = int(input("Digite um número: "))
        while num != 0:
            if (num % 2 == 0):
                somaPar += 1
            else:
                somaImpar += 1
            num = int(input("Digite um número: "))
        print("A soma dos números pares é ", somaPar," e a soma dos ímpares é ", somaImpar)
    except:
        print("Digite um número!")
main()