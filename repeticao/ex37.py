#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

cod_cliente = []
peso_cliente = []
alt_cliente = []

num_cliente = 1

cod = True
while(cod != 0):
    print("\nCliente de numero :{} \n".format(num_cliente))
    cod =  int(input("Informe o codigo do cliente: "))
    if cod == 0:
        break
    else:
        altura = float(input("Informe a altura do cliente: "))
        peso =  float(input("Informe o peso do cliente: "))
        cod_cliente.append(cod)
        peso_cliente.append(peso)
        alt_cliente.append(altura)
        num_cliente += 1

peso_max = peso_cliente.index(max(peso_cliente))
peso_min = peso_cliente.index(min(peso_cliente))
alt_max = alt_cliente.index(max(alt_cliente))
alt_min = alt_cliente.index(min(alt_cliente))

print("\n" * 3)

print("Código do cliente mais magro: {}".format(peso_cliente[peso_min]))
print("Código do cliente mais gordo: {}".format(peso_cliente[peso_max]))

print("Código do cliente mais baixo: {}".format(alt_cliente[alt_min]))
print("Código do cliente mais alto: {}".format(alt_cliente[alt_max]))

print("Média de pesos: {}".format(sum(peso_cliente)/ len(peso_cliente)))
print("Média de alturas: {}".format(sum(alt_cliente)/ len(alt_cliente)))



