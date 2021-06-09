
import random
import PySimpleGUI as sg 

class ChuteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentar_novamente = True

    def iniciar(self):
        layout = [
            [sg.Text('Seu Chute', size=(20,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20,10))]
        ]
        self.janela = sg.Window('Chute o numero!', Layout=layout)
        self.GerarNumeroAleatorio()
        try:
             while True: 
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor Mais Baixo')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais Alto')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:    
                            self.tentar_novamente = False
                            print('Parabéns Voce Acertou') 
                        break 
        except:
            print('Por Favor digitar apenas Números!') 
            self.iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_min,self.valor_max)    

chute = ChuteUmNumero()
chute.iniciar()        
        

