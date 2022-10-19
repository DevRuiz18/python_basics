#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
#cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e
#a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
#tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("Segue abaixa a tabela da super promoção de carnes\n")
print("------------------------------------------------------------------")
print("                     Até 5 Kg                Acima de 5 Kg")
print("File Duplo           R$ 4,90 por Kg          R$ 5,80 por Kg")
print("Alcatra              R$ 5,90 por Kg          R$ 6,80 por Kg")
print("Picanha              R$ 6,90 por Kg          R$ 7,80 por Kg")
print("------------------------------------------------------------------\n")

print("Para que todos possam aproveitar da promoção, cada cliente só poderá levar um tipo de carne!")
meat_type = input("Qual tipo de carne deseja levar? Pressione [F] para File Duplo, [A] para alcatra e [P] para picanha\n")

meat_amout = float(input("Informe quantos quilos você quer comprar: "))

card = int(input("Para realizar o pagamento por favor nos informe, você possui Cartão Tabajara? [1] para sim e [0] para não\n"))

if(meat_type == "F" or meat_type == "f"):
    if(meat_amout < 5):
        price = meat_amout * 4.9
    else:
        price = meat_amout * 5.8

    if(card ==  1):
        discount = (price/100) * 5
        final_price = price - discount
        print("---------------------------------------------------")
        print("Tipo da carne:               File Duplo;")
        print("Quantidade:",                meat_amout, "kilos;")
        print("Tipo de pagamento:           Cartão Tabajara;")
        print("Valor do desconto:",         discount)
        print("Valor final do produto:",    final_price)
        print("---------------------------------------------------")
    else:
        discount = 0
        final_price = price - discount
        print("---------------------------------------------------")
        print("Tipo da carne:               File Duplo;")
        print("Quantidade:",                meat_amout, "kilos;")
        print("Tipo de pagamento:           Outro;")
        print("Valor do desconto:",         discount)
        print("Valor final do produto:",    final_price)
        print("---------------------------------------------------")

elif(meat_type == "A" or meat_type == "a"):
    if (meat_amout < 5):
        price = meat_amout * 5.9
    else:
        price = meat_amout * 6.8

    if (card == 1):
        discount = (price / 100) * 5
        final_price = price - discount
        print("---------------------------------------------------")
        print("Tipo da carne:               Alcatra;")
        print("Quantidade:",                meat_amout, "kilos;")
        print("Tipo de pagamento:           Cartão Tabajara;")
        print("Valor do desconto:",         discount)
        print("Valor final do produto:",    final_price)
        print("---------------------------------------------------")
    else:
        discount = 0
        final_price = price - discount
        print("---------------------------------------------------")
        print("Tipo da carne:               Alcatra;")
        print("Quantidade:",                meat_amout, "kilos;")
        print("Tipo de pagamento:           Outro;")
        print("Valor do desconto:",         discount)
        print("Valor final do produto:",    final_price)
        print("---------------------------------------------------")

elif(meat_type == "P" or meat_type == "p"):
    if (meat_amout < 5):
        price = meat_amout * 6.9
    else:
        price = meat_amout * 7.8

    if (card == 1):
        discount = (price / 100) * 5
        final_price = price - discount
        print("---------------------------------------------------")
        print("Tipo da carne:               Picanha;")
        print("Quantidade:",                meat_amout, "kilos;")
        print("Tipo de pagamento:           Cartão Tabajara;")
        print("Valor do desconto:",         discount)
        print("Valor final do produto:",    final_price)
        print("---------------------------------------------------")
    else:
        discount = 0
        final_price = price - discount
        print("---------------------------------------------------")
        print("Tipo da carne:               Picanha;")
        print("Quantidade:",                meat_amout, "kilos;")
        print("Tipo de pagamento:           Outro;")
        print("Valor do desconto:",         discount)
        print("Valor final do produto:",    final_price)
        print("---------------------------------------------------")
else:
    print("Opa você informou algo errado!")