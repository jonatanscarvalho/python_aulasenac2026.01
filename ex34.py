# 10 méida de aluno
#ao ler mostrar se o aluno está aprovado ou reprovado


for i in range(0,10):
    media=int(input("Digite a sua média = >"))
    if media >=5:
        print(f"{i} -  aprovado ")
    else:
        print(f"{i} -  reprovado ")
    