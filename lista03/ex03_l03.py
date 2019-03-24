'''03 - Dado um número inteiro N, calcule e imprima os N primeiros da seqüência: 1, 3, 6, 10, 15, ... '''

n = int(input('Digite um número natural :'))

sequence = 0

for i in range(1, n+1):
    sequence += i
    print(sequence)
