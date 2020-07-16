def fatorial(k):
    '''(int) -> int
    Recebe um inteiro k e retorna o valor de k!

    Pré-condição: supõe que k é um número inteiro não negativo.
    '''

    k_fat = 1

    # CORPO DA FUNÇÃO
    if k == 0:
        return 1
    elif k < 0:
        return "Apenas números não negativos"
    else:
        while (k > 1):  
            k_fat = k_fat * k  
            k = k - 1
    
    return k_fat
def main():
# testes
    try:
        numero = int(input("Digite um número não negativo para mostrarmos o fatorial: "))
        while numero >= 0:
            print("Fatorial do número: ", fatorial(numero))
            try:
                numero = int(input("Se quiser encerrar, digite a letra K (maiúscula) , senão, digite outro número: "))
                if numero == 'K':
                    print("MUITO OBRIGADO POR USAR!!!")
            except:
                print("DIGITE A LETRA K SE QUISER ENCERRAR!!!")
    except:
        print('''
                DIGITE UM NÚMERO NÃO NEGATIVO!!!!!!!
        ''')
main()
