#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

prev1 = 1
prev2 = 1

print(prev1)
print(prev2)
prox = 0

while prox < 500:
    prox = prev1 + prev2
    print(prox)
    prev2 = prev1
    prev1 = prox
