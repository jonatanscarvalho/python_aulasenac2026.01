#Desenvola 
# que leia um valor
# e mostre a tabuada deste valor

# Solicita o número ao usuário
num = int(input("Digite um número para ver a tabuada: "))

print("-" * 12)
print(f"Tabuada de {num}:")

# Loop para calcular a tabuada de 1 a 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("-" * 12)



num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


