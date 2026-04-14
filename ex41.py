# desenvolva
# o usuario digite um numero
# mostrar a tabuada usando while


num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


i=0
v=int(input("Digite um número para ver a tabuada: "))
while i <= 10:
    m = i * v
    print(f"{num} x {i} = {num * i}")
    i=i + 1