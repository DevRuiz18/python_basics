#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes;

side1_str = input("Informe o primeiro lado do triângulo: ")
side1 = float(side1_str)

side2_str = input("Informe o segundo lado do triângulo: ")
side2 = float(side2_str)

side3_str = input("Informe o terceiro lado do triângulo: ")
side3 = float(side3_str)

if((side1+side2 > side3) or (side1+side3 > side2) or (side2+side3 > side1) ):
    if(side1 == side2 == side3):
        print("Os valores informados formam um triângulo Equilátero")
    elif(side1 == side2 or side1 == side3 or side2 == side3):
        print("Os valores informados formam um triângulo Isósceles")
    else:
        print("Os valores informados formam um triângulo Escaleno")
else:
    print("Os valores informados não formam um triângulo")

