#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

big = -999999999999999999
small = 99999999999999999
num = int(input("Informe quantos numeros deseja comparar: "))
sum = 0
gtg = False
for i in range(num):
    while(gtg == False):
        num_comp = int(input("Informe o {} numero: ".format(i+1)))
        if(num_comp > 0 and num_comp < 1000):
            gtg == True
        else:
            print("Numero excede os limites suportador, por favor informe outro")

    x = num_comp
    sum += x

    if(x > big):
        big = x
    if(small > x):
        small = x

print("maior: {} "
      "menor: {} "
      "soma: {}".format(big, small, sum))