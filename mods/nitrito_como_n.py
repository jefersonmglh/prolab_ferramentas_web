import pandas as pd

class Nitrito_N:


	def __init__(self, csv):

		
		self.csv = csv
		

	def calc(self):

		df = pd.read_csv(self.csv, sep = ",")
		df.drop(["Type", "WL543.0", "Comments"], axis=1, inplace=True)

		df['NO2 as N'] = df['Conc'].apply(lambda x: '<0.02' if x * 0.304 < 0.02
		                                               else round(x * 0.304, 2))
		
		no2 = df.to_html()
		return no2