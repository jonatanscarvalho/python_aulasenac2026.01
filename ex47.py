#  criar uma funcção que calcule 10% de um valor
#
#
def porc (x):
    p= x * 0.1
    return p
v=int(input("Digite um valor => "))
y=porc(v)
print(f"A porcentagem é {y} => ")


def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é Par."
    else:
        return f"O número {numero} é Ímpar."
    numero=int(input("Digite um valor => "))