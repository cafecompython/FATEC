'''08 - Dado um número inteiro positivo N, calcule e imprima o maior quadrado menor ou igual a N. Exemplo: N = 38, o maior quadrado que é menor ou igual a 30 é 36, imprimir 36.'''

N = int(input('Digite um número inteiro positivo: '))
q = 0
while q*q <= N:
    q+=1
q-=1
print(q*q)

