#QUE ENVIS UM VALOR
#PARA U,A FUNÇÃO
# SE INMPAR OU PAR
#
##
def par(a):
    if a % 2 == 0:
        return " Par."
    else:
        return "Ímpar."
v=int(input("Digite um valor => "))
y=par(v)
print(y)
    

