
#Desenvolva um programa que seja capar
#coletar uma sequencia de 5 número inteiros
#fornecidos pelo usuario. Ao final da leitura
#desses valores, o programa deve calcular o somatorio total e exibir o resultado na tela.

# 1 - coletar 5 numeros pelo usuario
# 2 - somar os valores
# 3 - exibir na tela

soma=0
for i in range(0,5):
    valor=int(input("Digite um número => "))
    soma=soma+valor
print(f"A soma dos valores digitados é => {soma}")
