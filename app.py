from mods.residuo_apos_evaporacao import Residuo
from mods.nitrato_como_n import Nitrato_N
from mods.nitrito_como_n import Nitrito_N
from mods.teor_de_umidade import Umidade
from mods.teor_de_cinzas import Cinzas
from mods.solucoes_acidas import *
import datetime

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

year = datetime.datetime.now().year

@app.route('/', methods=["POST", "GET"])
def init():
	res_resultado = ""
	if request.method == "POST":

		if 'res_tara' in request.form and 'res_volume' in request.form and 'res_final' in request.form:
		
			try:
				res_tara = float(request.form["res_tara"])
				res_volume = float(request.form["res_volume"])
				res_final = float(request.form["res_final"])		
				res = Residuo(res_tara,res_volume,res_final)
				res_resultado = res.calculo()
			except:
				res_resultado = '---ERRO: VALORES---'
			
			return render_template('index.html', year=year, res_resultado=res_resultado)

		elif 'nitra_csv_file' in request.files:

			try:
				f = request.files["nitra_csv_file"]
				nitra_csv_path = 'UPLOAD_FOLDER/no3.txt'
				f.save(nitra_csv_path)			

				nitra = Nitrato_N(nitra_csv_path)
				nitra_resultado = nitra.calc()	
			except:
				nitra_resultado = '---ERRO NO ARQUIVO---'
			
			return render_template('index.html', year=year, nitra_resultado=nitra_resultado)

		elif 'nitri_csv_file' in request.files:

			try:
				f = request.files["nitri_csv_file"]
				nitri_csv_path = 'UPLOAD_FOLDER/no2.txt'
				f.save(nitri_csv_path)			

				nitri = Nitrito_N(nitri_csv_path)
				nitri_resultado = nitri.calc()	
			except:
				nitri_resultado = '---ERRO NO ARQUIVO---'
			
			return render_template('index.html', year=year, nitri_resultado=nitri_resultado)

		elif 'umi_tara' in request.form and 'umi_massa1' in request.form and 'umi_massa2' in request.form:
			print('umi if')
			try:
				umi_tara = float(request.form["umi_tara"])
				umi_massa1 = float(request.form["umi_massa1"])
				umi_massa2 = float(request.form["umi_massa2"])
				umi = Umidade(umi_tara, umi_massa1, umi_massa2)
				umi_resultado = umi.calc()
			except:
				umi_resultado = '---ERRO: VALORES---'

			return render_template('index.html', year=year, umi_resultado=umi_resultado)

		elif 'cin_tara' in request.form and 'cin_massa1' in request.form and 'cin_massa2' in request.form:
			
			try:
				cin_tara = float(request.form["cin_tara"])
				cin_massa1 = float(request.form["cin_massa1"])
				cin_massa2 = float(request.form["cin_massa2"])
				cin = Cinzas(cin_tara, cin_massa1, cin_massa2)
				cin_resultado = cin.calc()
			except:
				cin_resultado = '---ERRO: VALORES---'

			return render_template('index.html', year=year, cin_resultado=cin_resultado)


		elif 'sol_acido' in request.form and 'sol_volume' in request.form and 'sol_concentracao' in request.form:

			try:
				sol_acido = request.form["sol_acido"]
				sol_volume = float(request.form["sol_volume"])
				sol_concentracao = float(request.form["sol_concentracao"])

				if sol_acido == "sulfurico":
					sol_acido_data = Sulfurico().data()
				elif sol_acido == "cloridrico":
					sol_acido_data = Cloridrico().data()
				else:
					sol_acido_data = Nitrico().data()

				sol_acido_nome = sol_acido_data.get('nome')
				sol_resultado = Solucoes_Acidas(acid_data=sol_acido_data, volume_final_sol=sol_volume, concentracao_sol=sol_concentracao).calc()

			except:
				sol_resultado = '---ERRO: VALORES---'
				sol_acido_nome = ''

			return render_template('index.html', year=year, sol_resultado=sol_resultado, acido_nome=sol_acido_nome)

	else:
		return render_template("index.html", year=year)


if __name__ == '__main__':
	app.run(debug=True)