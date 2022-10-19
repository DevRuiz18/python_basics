#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

valor_hora = input("Quanto você recebe por hora? ")

horas_trabalhadas = input("Quantas horas você trabalha por mês? ")

salario_total = float(valor_hora) * float(horas_trabalhadas)

print("Você recebeu nesse mês", salario_total, "reais")

