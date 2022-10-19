#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro
#   Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
#que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


liters = float(input("Informe quantos litros deseja abastecer: "))

gas_type_str = input("Informe qual tipo de combustivel deseja abastecer. Pressione [A] paara Álcool e [G] para gasolina\n")

if(gas_type_str == "A" or gas_type_str == "a"):
    if(liters >= 20):
        price = liters * 1.90 - ((1.9/100 * 3) * liters)
        print("O valor a ser pago por", liters, "litros de alcool será: R$", price, "reais")
    elif(liters < 20):
        price = liters * 1.90 - ((1.9 / 100 * 5) * liters)
        print("O valor a ser pago por", liters, "litros de alcool será: R$", price, "reais")
    else:
        print("Ops! Algo deu errado!")
elif(gas_type_str == "G" or gas_type_str == "g"):
    if (liters >= 20):
        price = liters * 2.5 - ((2.5 / 100 * 4) * liters)
        print("O valor a ser pago por", liters, "litros de gasolina será: R$", price, "reais")
    elif (liters < 20):
        price = liters * 2.5 - ((2.5 / 100 * 6) * liters)
        print("O valor a ser pago por", liters, "litros de gasolina será: R$", price, "reais")
    else:
        print("Ops! Algo deu errado!")
else:
    print("Ops! a Informação foi informada errada!")
