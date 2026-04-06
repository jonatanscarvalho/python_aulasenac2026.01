#Desenvolva um codido python
#que leia um valor
#dê um desconto de acordo com a tabela de valores abaixo
#tabela
# valor - desconto
#>500 - 20%
#100 a 499  - 15%
#<100 - 5%
#0.2 
v=float(input("Digite um valor =>"))
if v<100:
    p= v*0.05    # p = porcentagem
    d=v-p           # d = desconto
elif v < 499:
    p=v*0.15
    d=v-p
else:
    p=v*0.2
    d=v-p
print(f"o valor de {v} com desconto de {p} ficará em {d}")

