#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#  Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#  Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
#receberá ainda um desconto de 10% sobre este total.
#escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
#e escreva o valor a ser pago pelo cliente.

print("-------------------------------------------------------")
print("                     Tabela de preços")
print("             Até 5 Kg                Acima de 5 Kg")
print("Morango      R$ 2,50 por Kg          R$ 2,20 por Kg")
print("Maçã         R$ 1,80 por Kg          R$ 1,50 por Kg")
print("-------------------------------------------------------")
print()

choice = int(input("Hoje você vai querer comprar o que? pressione [1] para morango e [2] para maçã\n"))

amount = float(input("Informe quantos quilos deseja comprar: "))

if(choice == 1):
    if(amount >= 5):
        price_per_amount = amount * 2.50
    else:
        price_per_amount = amount * 2.20

    if(price_per_amount > 25.00 or amount > 8):
        final_price = price_per_amount + ((price_per_amount/100) * 10)
        print(amount, "kilos de morango ficará R$", final_price, "reais.")
    else:
        print(amount, "kilos de morango ficará R$", price_per_amount, "reais.")
elif(choice == 2):
    if (amount >= 5):
        price_per_amount = amount * 1.80
    else:
        price_per_amount = amount * 1.50

    if (price_per_amount > 25.00 or amount > 8):
        final_price = price_per_amount + ((price_per_amount / 100) * 10)
        print(amount, "kilos de maçã ficará R$", final_price, "reais.")
    else:
        print(amount, "kilos de maçã ficará R$", price_per_amount, "reais.")