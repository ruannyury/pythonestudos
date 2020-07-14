def main():
    a, b = 0, 1

    controle = int(input('Até que número queres a sequência?\n'))

    while a < controle:
        print(a, end = ',\n') #Evita a nova linha após a saída
        a, b = b, a + b

main()