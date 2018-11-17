# -*- CODING: UTF-8 -*-

import pandas as pd
import sys
import random

ativos = ["ABEV3", "BBAS3", "BBDC3", "BBDC4", "BRKM5", "CIEL3", "CMIG4",
		"CSNA3", "FJTA4", "GGBR4", "IGTA3", "ITSA3", "ITSA4",
		"ITUB4", "JBSS3", "KROT3", "LAME4", "LREN3", "PCAR4",
		"PETR3", "PETR4", "RADL3", "RAIL3", "RENT3", "SAPR4"]

df = pd.read_excel('Database.xlsx')

def encontrar():

	for i in range(len(ativos)):
		for j in range(i+1, len(ativos)):

			comprado = ativos[i]
			vendido = ativos[j]

			correlacao = df[comprado].corr(df[vendido], method='pearson')

			if (correlacao >= 0.8):
				print("[!] Razão encontrada: %s/%s -- %.3f" % (comprado, vendido, correlacao))
			else:
				continue

if __name__ == "__main__":
	encontrar()
	tempo = len(df.index)
	n_acoes = len(df.columns)
	print("[!] Período analisado: %d dias" % tempo)
	print("[!] Número de ações comparadas: %d" % n_acoes)
