class Carro:
    def __init__(self, marca, cor, modelo):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
    
    def Ligar(self):
        print('Carro ligando...')

    def Desligar(self):
        print('Carro desligando...')
    
    def ExibirInformacoesDesseCarro(self):
        print(self.marca,self.cor,self.modelo)

carro1 = Carro('BMW', 'Preto', '2020')
carro1.Ligar()
carro1.Desligar()
carro1.ExibirInformacoesDesseCarro()
        