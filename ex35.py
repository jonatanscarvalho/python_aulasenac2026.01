# que leia 5 idades
# diga se cada um é maior , menor de idade ou idoso


for i in range(0,5):
    idade=int(input("Digite a sua idade = >"))
    if idade <18:
        print(f"{i} - menor de idade ")
    elif idade <=65:
        print(f"{i} - maior de idade ")
    else: 
        print(f"{i} - idoso ")