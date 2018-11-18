# -*- CODING: UTF-8 -*-

import pandas as pd
import sys
import random

ativos = ["IBOV", "ABEV3", "ALPA4", "ALUP11", "ARZZ3", "AZUL4", "B3SA3",
		"BBAS3", "BBDC3", "BBDC4", "BBSE3", "BEEF3", "BIDI4",
		"BOVA11", "BRAP4", "BRDT3", "BRFS3", "BRKM5", "BRML3",
		"BRSR6", "BTOW3", "CCRO3", "CESP6", "CIEL3", "CMIG3",
		"CMIG4", "CPFE3", "CPLE6", "CRFB3", "CSAN3", "CSMG3", 
		"CSNA3", "CVCB3", "CYRE3", "DTEX3", "ECOR3", "EGIE3",
		"ELET3", "ELET6", "EMBR3", "ENBR3", "ENGI11", "EQTL3",
		"ESTC3", "EZTC3", "FIBR3", "FLRY3", "GFSA3", "GGBR4",
		"GOAU4", "GOLL4", "GRND3", "GUAR3", "HGTX3", "HYPE3",
		"IGTA3", "IRBR3", "ITSA4", "ITUB3", "ITUB4", "JBSS3",
		"KLBN11", "KROT3", "LAME3", "LAME4", "LIGT3", "LINX3",
		"LREN3", "MAGG3", "MDIA3", "MGLU3", "MRFG3", "MRVE3", 
		"MULT3", "MYPK3", "NATU3", "ODPV3", "OIBR3", "PCAR4",
		"PDGR3", "PETR3", "PETR4", "POMO4", "PSSA3", "QGEP3",
		"QUAL3", "RADL3", "RAIL3", "RAPT4", "RENT3", "RLOG3",
		"SANB11", "SANB11", "SAPR11", "SBSP3", "SEER3", "SLCE3",
		"SMTO3", "SMLS3", "SULA11", "SUZB3", "TAEE11", "TIET11",
		"TIMP3", "TOTS3", "TRPL4", "TUPY3", "UGPA3", "USIM5",
		"VALE3", "VIVR3", "VIVT4", "VVAR11", "WEGE3"]


df = pd.read_excel('Correlacoes.xlsm')

def encontrar():

	for i in range(len(ativos)):
		for j in range(i+1, len(ativos)):

			comprado = ativos[i]
			vendido = ativos[j]

			correlacao = df[comprado].corr(df[vendido], method='pearson')

			if (correlacao >= 0.75):
				print("[!] Razão encontrada: %s/%s -- %.3f" % (comprado, vendido, correlacao))
			else:
				continue

if __name__ == "__main__":
	encontrar()
	tempo = len(df.index)
	n_acoes = len(df.columns)
	print("[!] Período analisado: %d dias" % tempo)
	print("[!] Número de ações comparadas: %d" % n_acoes)
