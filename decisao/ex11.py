#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 280,00 (incluindo) : aumento de 20%
#   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#   salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#   o salário antes do reajuste;
#   o percentual de aumento aplicado;
#   o valor do aumento;
#   o novo salário, após o aumento.

wage_str = input("Informe seu salário: ")
wage = float(wage_str)

if(wage > 0 and wage <= 280):
    print("Salário antes do reajuste:", wage)
    print("O percentual aplicado: ", "20%")
    print("O valor do aumento: ", (wage/100) * 20)
    print("O novo salário após o aumento: ", wage + ((wage/100) * 20))
elif(wage > 280 and wage <= 700):
    print("Salário antes do reajuste:", wage)
    print("O percentual aplicado: ", "15%")
    print("O valor do aumento: ", (wage / 100) * 15)
    print("O novo salário após o aumento: ", wage + ((wage / 100) * 15))
elif(wage > 700 and wage <= 1500):
    print("Salário antes do reajuste:", wage)
    print("O percentual aplicado: ", "10%")
    print("O valor do aumento: ", (wage / 100) * 10)
    print("O novo salário após o aumento: ", wage + ((wage / 100) * 10))
elif(wage > 1500):
    print("Salário antes do reajuste:", wage)
    print("O percentual aplicado: ", "5%")
    print("O valor do aumento: ", (wage / 100) * 5)
    print("O novo salário após o aumento: ", wage + ((wage / 100) * 5))

