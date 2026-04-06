#Desenvolva um codigo python
#o usuario digita o seu genero
# m = masculinp f = feminino
# se o genero fo m print maculino senão irá imprimir feminino

g=input("Digite seu gênero m masculino ou f feminino =>")
if g == "m":
    print("Masculino")
else:
    print("Feminino")
    
# ele diferencia maiuscula de minuscula exemplo: A e a são diferentes
# quando comparar letras eu coloco em "a" aspas TEXTO PRECISA ESTAR ENTRE ASPAS
# - / TRASNFORMA EM TEXTO 
# se posso fazer calculo matematico é numero caso contrario é TEXTO e fica entre ASPAS
#OBS: / - viram textos

g=input("Digite seu gênero m masculino ou f feminino =>")
if g == "m" or g == "M":
    print("Masculino")
elif g =="f" or g== "F":
    print("Feminino")  
else:
    print("Gênero nao identificado")
print("Fim do código")
