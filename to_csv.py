import pandas as pd

# Caminho para o arquivo .xls
arquivo_xls = "Sample - Superstore.xls"

# Lê a primeira planilha do Excel
df = pd.read_excel(arquivo_xls)

# Exporta para CSV
df.to_csv("superstore.csv", index=False, encoding="utf-8")
print("Arquivo CSV criado com sucesso: superstore.csv")
