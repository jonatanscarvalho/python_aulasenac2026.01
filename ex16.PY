#Desenvola um codigo python parao exercito brasileiro
#onde irá verificar se o candidato estpa apto se alista
#ou não, para se alista deve ser do 
#sexo  masculino e maior de idade 
g=input("Digite seu gênero m para masculino ou f para feminino =>")
idade=float(input("Digite a sua idade => "))
if idade >=18 and g == "m":
    print(Apto para servir)
else:
    print(Não apto)