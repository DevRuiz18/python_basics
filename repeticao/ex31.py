#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
#Faça um programa que implemente uma caixa registradora rudimentar.
#O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
#Um valor zero deve ser informado pelo operador para indicar o final da compra.
#O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
#Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

#   Lojas Tabajara
#   Produto 1: R$ 2.20
#   Produto 2: R$ 5.80
#   Produto 3: R$ 0
#   Total: R$ 9.00
#   Dinheiro: R$ 20.00
#   Troco: R$ 11.00
#   ...

prices = []
amount = int(input("Informe quantos produtos deseja comprar: "))

for i in range(amount):
    price = float(input("Informe o valor do produto {}: ".format(i)))
    prices.append(price)

sum = int(0)
for i in range(amount):
    sum = prices[i] + sum

pay = float(input("Iforme o pagamento do cliente: "))

print("Lojas Tabajara")
for i in range(amount):
    print("Produto {}: R$ {}".format(i, prices[i]))
print("Total: R$ {}".format(sum))
print("Dinheiro: R$ {}".format(pay))
print("Troco: R$ {}".format(pay - sum))
