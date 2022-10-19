#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

horas_str = input("Informe quantas horas você trabalha no mês: ")
horas = int(horas_str)

valor_hora_str = input("Informe quanto você recebe por hora: ")
valor_hora = float(valor_hora_str)

salario_bruto = horas * valor_hora

if(salario_bruto > 0 and salario_bruto <= 900):
    print("Salário bruto: (", horas, "*", valor_hora, ")     : R$", salario_bruto)
    print("(-) IR (Isento)                 : R$ 00,00")
    print("(-) INSS (10%)                  : R$", (salario_bruto/100) * 10)
    print("Total de descontos              : R$", (salario_bruto/100) * 10)
    print("Salário liquido                 : R$", salario_bruto - ((salario_bruto/100) * 10))

elif(salario_bruto > 900 and salario_bruto <= 1500):
    print("Salário bruto: (", horas, "*", valor_hora, ")    : R$", salario_bruto)
    print("(-) IR (5%)                     : R$", (salario_bruto / 100) * 5)
    print("(-) INSS (10%)                  : R$", (salario_bruto / 100) * 10)
    print("Total de descontos              : R$", ((salario_bruto / 100) * 10) + (salario_bruto / 100) * 5)
    print("Salário liquido                 : R$", salario_bruto - ((salario_bruto / 100) * 10) - (salario_bruto / 100) * 5)

elif(salario_bruto > 1500 and salario_bruto <= 2500):
    print("Salário bruto: (", horas, "*", valor_hora, ")    : R$", salario_bruto)
    print("(-) IR (10%)                    : R$", (salario_bruto / 100) * 10)
    print("(-) INSS (10%)                  : R$", (salario_bruto / 100) * 10)
    print("Total de descontos              : R$", ((salario_bruto / 100) * 10) + (salario_bruto / 100) * 10)
    print("Salário liquido                 : R$",salario_bruto - ((salario_bruto / 100) * 10) - (salario_bruto / 100) * 10)

elif(salario_bruto > 2500):
    print("Salário bruto: (", horas, "*", valor_hora, ")    : R$", salario_bruto)
    print("(-) IR (20%)                    : R$", (salario_bruto / 100) * 20)
    print("(-) INSS (10%)                  : R$", (salario_bruto / 100) * 10)
    print("Total de descontos              : R$", ((salario_bruto / 100) * 10) + (salario_bruto / 100) * 20)
    print("Salário liquido                 : R$", salario_bruto - ((salario_bruto / 100) * 10) - (salario_bruto / 100) * 20)


