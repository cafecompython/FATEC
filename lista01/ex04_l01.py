'''04 - Dado um número inteiro N e uma lista de N números inteiros, imprima a soma dos números da lista.'''

N = input('Digite um número natural: ')
soma = 0
while N != 'fim':
    soma += int(N)
    N = input('Digite outro número natural ou "fim" para finalizar: ')    

print(soma)

    
