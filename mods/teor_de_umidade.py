
class Umidade:

    def __init__(self, tara, m1, m2):

        #tara - massa da cápsula vazia (em gramas)
        #massa_1 - massa da amostra (em gramas)
        #massa_2- massa da cápsula + amostra após secagem (em gramas)
        self.tara = tara
        self.massa_1 = m1
        self.massa_2 = m2
        self.lq = 1


    def calc(self):

        umidade = round((1 - ((self.massa_2 - self.tara) / self.massa_1)) * 100,2)
        if umidade < self.lq:
            umidade = "<1%"
        return umidade   

