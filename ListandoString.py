def ImpList(name):
    for i in name:
        print(i)

def main():
    stringlista = ('Uma string') 
    #Strings são sequências também:

    ImpList(stringlista)

    squares = [1,2,3,4,5]
    print(squares[:])
    print(squares + [5,4,3,2,1]) #Concatenação de listas
    #Listas são mutáveis:

    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64
    ImpList(cubes)

    #Adicionar no final da lista novos elementos:
    cubes.append(216) 
    cubes.append(7**3)
    ImpList(cubes)
    
    #Atribuição/remoção a fatias:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    ImpList(letters) 
    
    letters[2:5] = ['C', 'D', 'E']
    ImpList(letters) #Atribuir elementos numa fatia
    
    letters[2:5] = [] #Removendo fatia
    ImpList(letters)

    letters[:] = [] #Limpando string

    teste = list('teste'); #Transforma uma string em lista
    print(teste)

main()