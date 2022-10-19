#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
#Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Informe um numero para analisarmos se é primo ou não: "))
count = 0
for i in range(1, num+1):
    if(num%i == 0):
        count= count + 1

if(count == 2):
    print("O numero {} é primo.".format(num))
else:
    print("O numero {} não é primo.".format(num))