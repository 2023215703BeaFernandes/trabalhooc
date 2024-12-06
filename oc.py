import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# Carregar o arquivo CSV com uma única coluna
dados = pd.read_csv('wdbc.csv', sep=';')
dados = dados.to_numpy()
uns = np.ones ((dados.shape[0],1))
dados = valores = np.append(uns,dados, axis = 1)
print (dados)

