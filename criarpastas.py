from time import sleep
import pandas as pd
import os
from tkinter.filedialog import askopenfilename, askdirectory

print('='*30)
print(str('ESCOLHA O ARQUIVO EXCEL:').center(30))
sleep(0.5)
excel_name = askopenfilename()

print('='*30)
print(str('\nESCOLHA O CAMINHO PARA SALVAR AS PASTAS:').center(30))
sleep(0.5)
caminho_save = askdirectory()

df = pd.read_excel(excel_name)
nomes = df.values.T[0].tolist()

if '.xlsx' or '.xls' in excel_name:
    for i in nomes:
        path = os.path.join(f'{caminho_save}', i)
        os.mkdir(path)
print('='*30)
print(str('\nFIM\n').center(30))
print('='*30)
