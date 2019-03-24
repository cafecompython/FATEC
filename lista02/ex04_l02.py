'''04 - Construa um algoritmo para calcular o {pi} com a sequênica:'''

N = int(input('Digite o número de termos: '))
pi = 0
sinal = 1

for i in range(N):
    pi += sinal/((i*2)+1)
    sinal = -sinal

print(4*pi)
