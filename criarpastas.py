import pandas as pd
import os

file_loc = 'C:/Users/rafael.cardoso/OneDrive - PONTELAND DISTRIBUICAO SA/Área de Trabalho/DOCS_AM/Nomes_AM.xlsx'
df = pd.read_excel(file_loc)
nomes = df.values.T[0].tolist()

caminho = str(input('Insira o caminho de destino das pastas: ')).strip().replace('\\', '/')

for i in nomes:
    # INSERIR CAMINHO DE DESTINO:
    path = os.path.join(f'{caminho}', i)
    os.mkdir(path)
