#serve para importar o programa de leitura
import pandas as pd 
df = pd.read_csv('classicDisco.csv')

print(df.to_string()) 
#print(df.to_string())  # imprime os todos dados da planilha
#exibe as 5 primeiras linhas
#print(df.head())

#mostras as 5 ultimas linhas
print(df.tail(10))

# se eu quiser trazer linhas especifica eu uso print(df[inha:linha]) eu escolho as linhas que quero
print(df[10:15])

# pr saber quantas linhas e colunas existem no arquivo  print(df.shape)
print(df.shape)