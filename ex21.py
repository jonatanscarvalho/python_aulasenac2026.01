#desenvolva um codigo python
#que leia o salario de um funcionario
# se o salario for maior que 5000
#calcule o imposto de renda que sera 7.5% sobre o salario
# se for menor que 5000 nao paga imposto
# e se for maio que 8000 o imposto sera de 27%
# ao final mostre o salario bruto  o valor do imposto pago e o salario final
#elif se não caso contrario
#separar os enunciados por etapas
# 1
# 2
# 3


s=float(input(" Digite o seu salário =>"))
if s<=5000:
    i=0
elif s<=8000:  
    i=s*0.075
else:
    i=s*0.27
sf=s-i      # não preciso fazer varios calculos dentro das condições
print(f"Seu salário é {s} o valor do imposto é {i} e o valor com desconto é {sf}")
    