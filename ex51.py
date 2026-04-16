#funcçao que receba 
#dois numeros e
#retorne o maior dele


def maior (a, b):
    if a > b:
        return (a)
    else:
        return (b)
valor1=int(input(" Digite um valor => "))
valor2=int(input(" Digite um valor => "))
resultado = maior(valor1, valor2)
print(f"O maior valor digitado foi: {resultado}")