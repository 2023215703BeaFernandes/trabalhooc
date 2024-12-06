import numpy as np
import matplotlib
import pandas as pd

dados=pd.read_csv("wdbc.csv")
# Converter para numpy e adicionar coluna com np.append
valores = dados.to_numpy()
valores_com_1s = np.hstack((np.ones((valores.shape[0], 1)), valores))

print(valores_com_1s)
