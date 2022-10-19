#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

prev1 = 1
prev2 = 1

n = int(input("Infome até que posição deseja calcular a sequencia de Fibonacci: "))

print(prev1)
print(prev2)

i = 0

while i < n-2:
    prox = prev1 + prev2
    print(prox)
    prev2 = prev1
    prev1 = prox
    i += 1
