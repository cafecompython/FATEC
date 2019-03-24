'''05- Dados três números, A0, LIMITE e RAZÃO, imprima todos os números gerados pela PA (Progressão Aritmética)
cujos valores são menores que o LIMITE. A PA tem valor inicial A0 e razão RAZÃO.'''

A0 = int(input('Digite o valor inicial da PA (A0): '))
LIMITE = int(input('Digite o valor do limite da PA (LIMITE): '))
RAZAO = int(input('Digite a razão da PA (RAZÃO): '))

print(f'A0 = {A0}; LIMITE = {LIMITE}; RAZÃO = {RAZAO}')

for n in range(A0, LIMITE, RAZAO):
    print(n)
