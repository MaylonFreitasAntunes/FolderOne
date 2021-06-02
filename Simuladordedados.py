#Simulador de dados:
#Simula número de 1 a 6.
import random
from PySimpleGUI import PySimpleGUI as sg

class SimuladordeDado:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
        
        self.layout = [
           [sg.Text('Jogar o Dado?')],
           [sg.Button('Sim'),sg.Button('Nao')]
        ]
        
   
    def iniciar(self):
         self.janela = sg.Window('Simulador de Dado', Layout=self.layout)
         self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Nao' or self.eventos == 'n':
                print('Obrigado pela participação')
            else:
                print('Por favor Digitar Sim ou Não')
        except:
            print('Erro')      
         

    def GerarValorDoDado(self):
        print(random.randint(self.valor_min,self.valor_max))   

simulador = SimuladordeDado()
simulador.iniciar()      

