def main():
    import random
    print('''
        Bem vindo ao simulador de dado! Prazer.
    ''')
    try:
        control = int(input("Digite qualquer número para começar: "))
    
        while control != 0:
            dado = random.randint(1, 9)
            print("Valor aleatório: ",dado)      
            control = int(input("Se quiser parar digite zero, senão, digite qualquer outro número: "))
        print('''
            MUITO OBRIGADO POR UTILIZAR O DADO SIMULATOR!!!! ACABAS DE MOSTRAR
            QUE NÃO TENS DADO EM CASA RSRSRS.
            ASS: RUANN YURY
        ''')
    except:
        print("DIGITE UM NÚMERO!!!!!!")

main()