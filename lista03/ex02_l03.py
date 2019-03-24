'''02 - Dado um numero natural N, determinar o número harmônico H definido por: '''

n = int(input('Digite um número natural: '))

h = 0

for k in range(1, n+1):
    h += 1/k

print(f'Número harmônico: {h}')
