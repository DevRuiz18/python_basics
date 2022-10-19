#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.

n = int(input("Informe o total de CDs da sua coleção: "))
value_sum = 0

for i in range(n):
    value = float(input("O valor do CD de etiqueta {}: ".format(i+1)))
    value_sum += value

print("O valor total da coleção é {}".format(value_sum))
print("O valor medio de cada item da coleção é {}".format(value_sum/n))