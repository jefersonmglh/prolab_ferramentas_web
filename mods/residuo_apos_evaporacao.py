class Residuo:
    def __init__(self, minicial, vol, mfinal):
        self.tara = minicial
        self.volume = vol
        self.final = mfinal        


    def calculo(self):
        resposta = round(1e6 * ((self.final - self.tara)/self.volume),2)
        return resposta
