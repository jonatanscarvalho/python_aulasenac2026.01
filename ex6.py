# Desenvolva um codigo que armazene a altura de uma pessoa e o peso calcule o IMC indice de massa corporal
# usando valores reais (float) para altura ao final mostre o IMC  IMC=PESO/(ALTURA*ALTURA)
a=1.80
p=85
imc=p/(a*a)
print(f"O seu IMC é =>{imc}")

# Desenvolver por parte  atribuir a altura, depois o peso, fazer o calculo e por ultimo printar.
#p=i put("Digite o seu peso =>")
#OBS: O input - somente captura textos
#float converte um texto em valor real
#input recebe dados mas apenas em texto e usando o float eu converto em numero real


a=float(input("Digite o seu peso =>"))
p=float(input("Digite o seu altura =>"))
imc=p/(a*a)
print(f"O seu IMC é =>{imc}")


#calcular media de um aluno, necessario digitar as duas notas bimestrais e calcular a media entre as duas nota
#ao final mostrar a media
n1=float(input("Digite a sua primeira nota =>"))
n2=float(input("Digite a sua segunda nota =>"))
media=n1+n2/2
print(f"O seu IMC é =>{media}")
