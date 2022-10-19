#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#   Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#   Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#   A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario =  float(input("Informe o salario inicial do funcionario: "))

ano_comeco = 1996
ano_atual = 2022

adcional = 1.5

for i in range(ano_comeco, ano_atual+1):
    print("O salario no ano de {} sera {}".format(i, salario+((salario/100) * adcional)))
    adcional = adcional * 2
