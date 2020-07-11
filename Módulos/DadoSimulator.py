def main():
    import random #Importa a biblioteca RANDOM, que gera valores aleatórios
    print('''
        Bem vindo ao simulador de dado! Prazer.
    ''')
    try: #Captura uma exceção caso o usuário digite algo diferente de um número
        control = int(input("Digite qualquer número para começar: "))
    
        while control != 0: #Enquanto o número digitado não for zero ele gera valores aleatórios entre 1 e 6
            dado = random.randint(1, 6) #Chamada 
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