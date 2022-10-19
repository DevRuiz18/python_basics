#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$

valor_hora = input("Quanto você recebe por hora? ")

horas_trabalhadas = input("Quantas horas você trabalha por mês? ")

salario_total = float(valor_hora) * float(horas_trabalhadas)
print("Salario bruto", salario_total, "reais")

salario_IR = ((salario_total/100) * 11)
print("IR", salario_IR, "reais")

salario_INSS = ((salario_total/100) * 8)
print("INSS", salario_INSS, "reais")

salario_sindicato = ((salario_total/100) * 5)
print("Sindicato", salario_sindicato, "reais")

salario_liquido = salario_total - salario_IR - salario_INSS - salario_sindicato
print("Salario liquido", salario_liquido, "reais")

