#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#   Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#   Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#   Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#   Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a_str = input("Informe o valor de A para a formula ax2 + bx + c : ")
a = int(a_str)

if(a == 0):
    print("Como o valor de A é zero, não se trata de uma equação de segundo grau.")
    exit()

b_str = input("Informe o valor de B para a formula ax2 + bx + c : ")
b = int(b_str)

c_str = input("Informe o valor de C para a formula ax2 + bx + c : ")
c = int(c_str)

delta = (b * b) - (4 * a * c)

if(delta < 0):
    print("A resultado de delta é negativo, logo a equação não possui raizes reais.")
    exit()

elif(delta == 0):
    print("A resultado de delta é 0, logo a equação possui apenas uma raiz real. Sendo essa:", delta ** 0.5)

else:
    print("Delta é positivo e tem duas raizes reais sendo elas: +", delta ** 0.5, "e -", delta ** 0.5)

