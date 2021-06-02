
import random

class ChuteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentar_novamente = True

    def iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            try:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor Mais Baixo')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais Alto')
                    self.PedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:    
                    self.tentar_novamente == False
                    print('Parabéns Voce Acertou') 
                    break 
            except:
                print('Por Favor digitar apenas Números!') 
                self.PedirValorAleatorio()  
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um Número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_min,self.valor_max)    

chute = ChuteUmNumero()
chute.iniciar()        
        

