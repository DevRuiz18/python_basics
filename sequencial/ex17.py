#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
#para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

qntd_metros = input("Iforme metros você deseja pintar: ")
metros = int(qntd_metros)

qntd_litros = metros / 6

qntd_latas1 = qntd_litros / 18
qntd_latas2 = qntd_litros / 3.6

print("O valor a ser pago apenas em latas de 18L será:", int(qntd_latas1) * 80)
print("O valor a ser pago apenas em latas de 3.6L será:", int(qntd_latas1) * 25)





