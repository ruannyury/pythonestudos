def main():
    from math import sqrt, floor, ceil
    num = int(input("Digite um número: "))
    raiz = sqrt(num)
    print("A raiz de {} é igual a {:.2f}".format(num, raiz) #Arredonda pra cima
    print("(Arredondando pra cima) A raiz de {} é igual a {}".format(num, ceil(raiz))) #Arredonda pra cima
    print("(Arredondando pra baixo) A raiz de {} é igual a {}".format(num, floor(raiz))) #Arredonda pra baixo


main()