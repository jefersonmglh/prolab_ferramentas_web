import pandas as pd

class Nitrato_N:


	def __init__(self, csv):

		
		self.csv = csv
		

	def calc(self):

		df = pd.read_csv(self.csv, sep = ",")
		df.drop(["Type", "WL220,0", "Comments"], axis=1, inplace=True)

		df['NO3 as N'] = df['Conc'].apply(lambda x: '<1' if x * 0.2259 < 1
		                                               else round(x * 0.2259, 1))
		
		no3 = df.to_html()
		return no3