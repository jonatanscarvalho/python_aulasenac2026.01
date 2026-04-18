import pandas as pd

dados = { 
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salarios': [1000, 2000, 3000, 4000]
}

dados_bi = pd.DataFrame(dados)
print(dados_bi) 
#com o head () eu escolho quais linhas quero imprimir
#print(dados_bi.head(3)) 
# 
##print(dados_bi.tail(1))  
#print(dados_bi.shape)

#para exportar os arquivos para o csv
# 'meus dados" eu crio o nome do arquivo e salvo
dados_bi.to_csv('meus_dados.csv', index=False, sep=';', encoding= 'utf-8')
print("Arquivo exportado com sucesso")