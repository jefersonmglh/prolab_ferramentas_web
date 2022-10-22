class Sulfurico:
    def __init__(self):

        self.massamolar = 98.079
        self.densidade = 1.83
        self.pureza = 98
    def data(self):
        return {
            "massa_molar": self.massamolar,
            "densidade": self.densidade,
            "pureza": self.pureza
        }

class Cloridrico:
    def __init__(self):

        self.massamolar = 36.458
        self.densidade = 1.18
        self.pureza = 37
    def data(self):
        return {
            "massa_molar": self.massamolar,
            "densidade": self.densidade,
            "pureza": self.pureza
        }

class Nitrico():
    def __init__(self):

        self.massamolar = 63.01
        self.densidade = 1.51
        self.pureza = 65
    def data(self):
        return {
            "massa_molar": self.massamolar,
            "densidade": self.densidade,
            "pureza": self.pureza
        }




class Solucoes_Acidas:

    def __init__(self, acid_data,volume_final_sol, concentracao_sol):
        self.massa_molar = acid_data.get('massa_molar')
        self.densidade = acid_data.get('densidade')
        self.pureza = acid_data.get('pureza')
        self.volume_f = volume_final_sol
        self.concentracao = concentracao_sol

    def calc(self):
        volume_i_acid = round(((100 * self.massa_molar * self.concentracao * self.volume_f) / (self.pureza * self.densidade)), 2)
        return volume_i_acid







