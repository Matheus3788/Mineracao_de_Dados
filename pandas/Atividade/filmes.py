import pandas as pd
import json

resultados = []

filmes = pd.read_csv("tmdb_5000_credits.csv")

# Leitura do arquivo - head()
print(filmes.head())
print(filmes.columns.to_list())
print(filmes.info())

#Demonstrar os dados das colunas ['title',''cast"]
df_col = filmes[['title', 'cast']]
print(df_col.head())

# Para efeito didático, utilizarei somente as 5 primeiras linhas
df_5 = filmes.head(5)


#Demonstrar a disposição de nomes de alguns atores, baseado em seus respectivos filmes;
for index, row in df_5.iterrows():
    titulo = row['title']
    cast_json = row['cast']
    
    # A coluna 'cast' é um JSON
    cast_lista = json.loads(cast_json)
    
    # Extrair os nomes dos atores(Limitado a 5 atores por filme)
    atores = [ator['name'] for ator in cast_lista][:5]
    
    for ator in atores:
        resultados.append({'title': titulo, 'cast': ator})


df_resultado = pd.DataFrame(resultados)
df_resultado.to_csv("filme_e_atores.csv", index=False)
print(df_resultado)