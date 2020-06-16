#-*- coding: utf-8 -*-
temp = 'Digite a temperatura em Fahrenheit\n'
#capturar uma exceção:
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Por favor, digite um número!')
