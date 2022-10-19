#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
#e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

amount = int(input("Quantas temperaturas deseja medir: "))

smallest = 900000
biggest = 0

sum = 0

for i in range(amount):
    temp = float(input("Informe uma temeperatura: "))
    sum = sum + temp
    if(temp < smallest):
        smallest = temp
    elif(temp > biggest):
        biggest = temp

print("O maior: {}".format(biggest))

print("O menor: {}".format(smallest))

print("A media das temeperaturas: {}".format(sum/amount))