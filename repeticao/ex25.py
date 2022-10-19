#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
#e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input("Informe o numero de pessoas que serao cadastradas as idades: "))
age_sum = 0

for i in range(n):
    age = int(input("Informe a idade da pessoa '{}': ".format(i+1)))
    age_sum += age

if(age_sum/n > 0 and age_sum/n < 26):
    print("A media de idade da amostra de populacao é {}, logo são classificados como jovem.".format(age_sum/n))
elif(age_sum/n > 25 and age_sum/n < 61):
    print("A media de idade da amostra de populacao é {}, logo são classificados como adulta.".format(age_sum/n))
else:
    print("A media de idade da amostra de populacao é {}, logo são classificados como idosa.".format(age_sum / n))
