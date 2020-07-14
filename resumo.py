# -*- coding: utf-8 -*-

##Resumo

#Atribuição:
message = 'Olá mundo'
print(message)
print("Olá mundo")

#Operações:
print(2 / 2)
print(4 // 3)
    #Exponenciação:
print(2 ** 3)
    #resto:
print(10 % 3)

#Operadores relacionais:
x = 2
y = 3
soma = x + y
print(x == y) #False
print(x < y) #True
print(soma == x) #False

#Operadores Lógicos:
print(x == y and x == soma) #False
print(x == y or y == 3) #True

#Operadores Condicionais:
if x < y:
    print("A variável X é menor\n")
elif x > y:
    print("A variável Y é menor\n")
elif x == y:
    print("As variáveis são iguais\n")
elif x != y:
    print("As variáveis são diferentes\n")

#Laços de repetição:
x = 1
while x <= 10:
    print(x)
    x += 1 #x = x + 1
lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [1,"biscoito","Ruann",7]
for i in lista1: #Ele percorre a lista1
    print(i)

for i in range(10): #Imprime de 0 a 9; uma contagem
    print(i)

for i in range(10,20): #Imprime de 10 a 19
    print(i)

for i in range(10,20,2): #Imprime de 10 a 20 de 2 em 2
    print(i)

#Strings:
    #Concatenação:
r = "Ruann"
y = "Yury"
concatenacao = r + " " + y
print(r + y)
    #Concatenação automática:
frase = ('Primeira parte da frase' 
         'Segunda parte da frase')

    #Multiplicando strings:
primeira = 'Ruann\n'
segunda = 3
print(primeira*segunda)

    #Tamanho de uma string:
tamanho = len(concatenacao)
print(tamanho)

    #Exibir oque estiver na posição:
print(r[2])

    #Imprime um pedaço da string:
print(r[0:2])
print(r[1:])

    #Pedir para o usuário escreva algo:
nome = input('Qual o seu nome, mestre?\n')
print("Seja bem vindo, ", nome)
idade = input('Qual a sua idade?\n')
print(int(idade))

############# Método!!!!!!:
print(concatenacao.lower()) #Função LOWER deixa tudo minúsculo
print(concatenacao.upper()) #Função UPPER deixa tudo maiúsculo
print(concatenacao.strip()) #Função STRIP remove espaços e caracteres especiais indesejados
