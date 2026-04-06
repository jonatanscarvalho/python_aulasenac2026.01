#Desenvolva um codigo python
#que leia 3 valores 
#ao final mostre qual o valor maior entre eles
#
v1=int(input("Digite um valor V1 => "))
v2=int(input("Digite um valor V2 => "))
v3=int(input("Digite um valor V3 => "))
if v1 > v2  and v1 > v3:
    print(f"{v1} é maior que {v2} e {v3}")
elif v2 > v1 and v2 > v3:
    print(f"{v2} é maior que {v1} e {v3}")
else:
    print(f"{v3} é maior que {v1} e {v2}")
print("Fim do código")

# não precisa colocar entre "" o que não for para print