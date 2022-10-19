#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1_str = input("Informe o preço do primeiro produto: ")
preco1 = float(preco1_str)

preco2_str = input("Informe o preço do segundo produto: ")
preco2 = float(preco2_str)

preco3_str = input("Informe o preço do terceiro produto: ")
preco3 = float(preco3_str)

if(preco1 < preco2 and preco1 < preco3):
    print("O primeiro produto está mais em conta")
elif(preco2 < preco1 and preco2 < preco3):
    print("O segundo produto está mais em conta")
else:
    print("O terceiro produto está mais em conta")