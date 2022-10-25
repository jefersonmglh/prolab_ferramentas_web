class Residuo:
    def __init__(self, minicial, vol, mfinal):
        self.tara = minicial
        self.volume = vol
        self.final = mfinal      
        self.lq = 0.1  


    def calculo(self):
        resposta = round(1e6 * ((self.final - self.tara)/self.volume),2)

        if resposta < self.lq:
            resposta = "<0.1 mg/L"
        return resposta
