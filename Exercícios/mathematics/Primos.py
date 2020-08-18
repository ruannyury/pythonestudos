def main():
    num = int(input('Digite um número: '))
    total = 0
    for contador in range(1, num + 1):  # Não inclusive
        if num % contador == 0:
            print('\033[33m', end='')
            total += 1
        else:
            print('\033[31m', end='')
        print('{} '.format(contador), end='')
    print(f'\nO {num} foi divisível {total} vezes')


main()
