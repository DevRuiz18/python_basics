#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_str = input("Informe quantos metros quadrados tem a area que deseja ser pintada: ")

area = float(area_str)

quantidade_litros = area / 3

qntd_latas = quantidade_litros / 18

latas = int(qntd_latas)

preco_total = int(qntd_latas) * 80

print("Você devera comprar", latas, "e isso lhe custará", int(preco_total))