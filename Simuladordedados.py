#Simulador de dados:
#Simula número de 1 té 6.
import random

class SimuladordeDado:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

    def GerarValorDoDado(self):
        print(random.randint(self.valor_min,self.valor_max))    
   
    def iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'nao' or resposta == 'n':
                print('Obrigado pela participação')
            else:
                print('Por favor Digitar Sim ou Não')
        except:
            print('Ocorreu um erro')

         

simulador = SimuladordeDado()
simulador.iniciar()      

