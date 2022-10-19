#Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input("Informe quantas notas serão usadas para a média: "))
notas = 0
for i in range(n):
    nota = float(input("Informe a {}º nota: ".format(i+1)))
    notas += nota

print("A média das {} notas é {}".format(n, notas/n))