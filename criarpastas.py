import pandas as pd
import os

excel_name = str(input('Insira o nome do arquivo Excel (Com a extensão):\n'))
file_loc = str(input('Insira o caminho do arquivo Excel:\n')).strip().replace('\\', '/')
loc_full = file_loc + ('/'+excel_name)
df = pd.read_excel(loc_full)
nomes = df.values.T[0].tolist()
caminho = str(input('Insira o caminho de destino das pastas:\n')).strip().replace('\\', '/')

for i in nomes:
    path = os.path.join(f'{caminho}', i)
    os.mkdir(path)
