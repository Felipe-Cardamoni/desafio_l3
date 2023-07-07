import pandas as pd
from pandas.io.json import json_normalize

# Dados do arquivo JSON
data = [
   {
      "CreateDate":"2021-05-24T20:21:34.79",
      "EmissionDate":"2021-05-24T00:00:00",
      "Discount":0.0,
      "NFeNumber":501,
      "NFeID":1,
      "ItemList":[
         {
            "ProductName":"Rice",
            "Value":35.55,
            "Quantity":2
         },
         {
            "ProductName":"Flour",
            "Value":11.55,
            "Quantity":5
         },
         {
            "ProductName":"Bean",
            "Value":27.15,
            "Quantity":7
         }
      ]
   },
   {
      "CreateDate":"2021-05-24T20:21:34.79",
      "EmissionDate":"2021-05-24T00:00:00",
      "Discount":0.0,
      "NFeNumber":502,
      "NFeID":2,
      "ItemList":[
         {
            "ProductName":"Tomate",
            "Value":12.25,
            "Quantity":10
         },
         {
            "ProductName":"Pasta",
            "Value":7.55,
            "Quantity":5
         }
      ]
   },
   {
      "CreateDate":"2021-05-24T20:21:34.79",
      "EmissionDate":"2021-05-24T00:00:00",
      "Discount":0.0,
      "NFeNumber":503,
      "NFeID":3,
      "ItemList":[
         {
            "ProductName":"Beer",
            "Value":9.00,
            "Quantity":6
         },
         {
            "ProductName":"French fries",
            "Value":10.99,
            "Quantity":2
         },
         {
            "ProductName":"Ice cream",
            "Value":27.15,
            "Quantity":1
         }
      ]
   }
]

# Transforma o JSON em um DataFrame
df = pd.json_normalize(data, 'ItemList', ['NFeNumber', 'CreateDate', 'EmissionDate', 'Discount', 'NFeID'])

# Exibe o DataFrame
print("DataFrame:")
print(df)

# Divide o DataFrame em dois: um com os dados da nota fiscal e outro com os itens
df_nfe = df[['NFeNumber', 'CreateDate', 'EmissionDate', 'Discount', 'NFeID']].drop_duplicates()
df_itens = df.drop(columns=['NFeNumber', 'CreateDate', 'EmissionDate', 'Discount', 'NFeID'])

# Exibe o DataFrame de notas fiscais
print("\nDataFrame de Notas Fiscais:")
print(df_nfe)

# Exibe o DataFrame de itens
print("\nDataFrame de Itens:")
print(df_itens)
