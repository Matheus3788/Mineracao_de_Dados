import pandas as pd

# automoveis = pd.read_csv("marcas-carros.csv")

automoveis = pd.read_csv("marcas-carros.csv", sep=';')

print(automoveis.head())

print(automoveis.info())

print(automoveis.columns.to_list())