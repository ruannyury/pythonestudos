#O programa pede ao usuário uma pontuação entre 0.0 e 1.0.
#Se a pontuação for fora do intervalo, mostra uma mensagem de erro.
#Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota usando
#a seguinte tabela.

#Pontuação    Nota
# >= 0.9       A
# >= 0.8       B
# >= 0.7       C
# >= 0.6       D
#  < 0.6       F

#-*- coding: utf-8 -*-

try:
    pontuacao = input("Digite uma pontuação entre 0.0 e 1.0: ")
    pontuacao = float(pontuacao)

    if pontuacao > 1.0:
        print("Número acima da escala!\n")
    elif pontuacao >= 0.9:
        print("Nota: A!\n")
    elif pontuacao >= 0.8:
        print("Nota B.\n")
    elif pontuacao >= 0.7:
        print("Nota C.\n")
    elif pontuacao >= 0.6:
        print("Nota D.\n")
    elif pontuacao < 0.6 and pontuacao >= 0:
        print("Nota F!\n")
    elif pontuacao < 0:
        print("Número abaixo da escala!\n")
except:
    print("Erro. Digite um numeral!")
