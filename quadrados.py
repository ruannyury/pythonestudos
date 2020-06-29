#Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados
def main():
    num = int(input("Digite um número: "))
    while num != 0:
        quadrado = num * num
        print(num, "ao quadrado é", quadrado)
        num = int(input("Digite um número: "))

main()