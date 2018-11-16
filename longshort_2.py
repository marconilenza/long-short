import pandas as pd
import sys

df = pd.read_excel('Database.xlsx')

comprado = str(input("[!] Digite o nome da ação (long): ")).upper()
vendido = str(input("[!] Digite o nome da ação (short): ")).upper()

try:
	correlacao = df[comprado].corr(df[vendido])
except KeyError:
	print("[-] Algum dos ativos não consta na planilha.")
	sys.exit(1)

dp_c = df[comprado].std()
dp_v = df[vendido].std()

print("[+] Razão entre os preços dos ativos: %.4f" % correlacao)
print("[+] Desvio-padrão de %s: %.3f" % (comprado, dp_c))
print("[+] Desvio-padrão de %s: %.3f" % (vendido, dp_v))
