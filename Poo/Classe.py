class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video): #Acessar as propriedades/métodos de uma instância
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    
    def Ligar(self):
        print('Estou ligando')
    
    def Desligar(self):
        print('Estou desligando')
    
    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Asus', '16gb', 'Nividia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()

