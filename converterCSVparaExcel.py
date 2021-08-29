import numpy as np
import pandas as pd

# Abrindo o arquivo csv
df_new = pd.read_csv('pathDoArquivoCSV')

# Salvar arquivo xlsx
myfile = pd.ExcelWriter('excel.xlsx')
df_new.to_excel(myfile, index=False)
myfile.save()
