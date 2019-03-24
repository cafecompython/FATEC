'''05 - Dada a seqüência, calcular o cos:'''

n = int(input('n: '))
x = float(input('x: '))

cos = 1
fat = 1
sinal = -1

for i in range(2,n+1,2):
    fat = i * (i-1)*fat
    cos +=((x**i)/fat)*sinal
    sinal = -sinal

print(cos)
