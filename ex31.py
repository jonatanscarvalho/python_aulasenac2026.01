#desenvola um codigo 
# o usuario digita 5 valors
# depois de digitar informar se o valor é par ou impar
# == 0 par

for i in range(0,5):
    x=int(input("Digite um valor => "))
    r = x % 2
    if r % 2 == 0:
        input(f"o valor {x} é par => ")
    else:
        input(f"o valor {x} é impar =>")

