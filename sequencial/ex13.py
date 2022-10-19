#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7

sexo = input("Informe seu sexo: ")

if(sexo == "masculino"):
    h = input("Masculino, Informe sua altura: ")
    peso_ideal = (72.7 * float(h)) - 58
else:
    h = input("Feminino, Informe sua altura: ")
    peso_ideal = (62.1 * float(h)) - 44.7

print("Seu peso ideal é:", peso_ideal)

