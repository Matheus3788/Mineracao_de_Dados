# pip install pandas
import pandas as pd

df = pd.DataFrame(
    {
        "Nome:":{
            0: "João",
            1: "Maria",
            2: "José"
        },
        "Escolaridade:":{
            0:"Ensino Médio",
            1:"Ensino Superior",
            2:"Ensino Fundamental"
        }
    }
)


print(df)

df.to_csv("dados.csv", index=False)