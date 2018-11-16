# -*- CODING: UTF-8 -*-

import pandas as pd
import sys
import random

ativos = ["ABEV3", "BBAS3", "BBDC3", "BBDC4", "BRKM5", "CIEL3", "CMIG4",
		"CSNA3", "FJTA4", "GGBR4", "IGTA3", "ITSA3", "ITSA4",
		"ITUB4", "JBSS3", "KROT3", "LAME4", "LREN3", "PCAR4",
		"PETR3", "PETR4", "RADL3", "RAIL3", "RENT3", "SAPR4"]

try:
	dias = int(input("[+] Digite o número de dias que deseja analisar: "))
except ValueError:
	print("[!] Digite apenas um número inteiro.")
	sys.exit(1)

df = pd.read_excel('Database.xlsx')

def encontrar():

	for i in range(len(ativos)):
		for j in range(i+1, len(ativos)):
			comprado = ativos[i]
			vendido = ativos[j]

			media_c = ((df[comprado].sum()) / dias)
			media_v = ((df[vendido].sum()) / dias)

			razao = (media_c / media_v)

			if (razao >= 0.8):
				print("[!] Razão encontrada: %s/%s -- %.3f" % (comprado, vendido, razao))
			else:
				continue

if __name__ == "__main__":
	mov = ""
	mov += random.choice("-\|/-\|/")
	for m in mov:
		sys.stdout.write("[%s] Encontrando razões maiores ou iguais a 0.8... \r" % m)
		sys.stdout.flush()

	encontrar()
