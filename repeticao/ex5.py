#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.

country_a = 80000
country_b = 200000
count = 0

country_a =int(input("Informe a quantidade do primeiro pais: "))
country_b =int(input("Informe a quantidade do segundo pais: "))


if(country_a < country_b):
    while (country_a <= country_b):
        country_a += country_a * 0.03
        country_b += country_b * 0.015
        count += 1
elif(country_a > country_b):
    while(country_b <= country_a):
        country_a += country_a * 0.03
        country_b += country_b * 0.015
        count += 1

print("O primeiro pais ultrapassara o segundo em {} anos".format(count))