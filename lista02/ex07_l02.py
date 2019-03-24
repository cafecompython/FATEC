''' 07 - Dado um número inteiro N (N >= 10), verificar se este tem dois algarismos adjacentes iguais.'''

n = int(input('Digite um número maior que 10: '))

ant = None
d = 0

while n > 0:
    d = n%10
    n= n//10

    if d is ant:
        print(f'Números adjacentes iguais {d} e {ant}.')
    else:
        print(f'Números adjacentes diferentes {d} e {ant}.')

    ant = d

