class fibonacci:
    def __init__(self):
        self.a,self.b = 1,1

    def iniciar(self):  
        while self.a < 1000:
            print(self.a, end='> ')
            self.a,self.b = self.b,self.a+self.b


fibo = fibonacci()
fibo.iniciar()