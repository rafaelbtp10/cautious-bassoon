import pandas as pd
import os

file_loc = str(input(r'Insira o caminho do arquivo Excel:\n'))
df = pd.read_excel(file_loc)
nomes = df.values.T[0].tolist()

caminho = str(input(r'Insira o caminho de destino das pastas:\n')).strip()

for i in nomes:
    path = os.path.join(f'{caminho}', i)
    os.mkdir(path)
