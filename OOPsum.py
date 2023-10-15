class Calculo: #Soma de Parcelas
    def __init__(self, parcela1, parcela2):
        self.parcela1 = parcela1
        self.parcela2 = parcela2
    def calcular(self):
        return self.parcela1 + self.parcela2
x= 10
y = 30
calculo1 = Calculo(x, y)

calculo1.calcular()
print(calculo1.calcular())