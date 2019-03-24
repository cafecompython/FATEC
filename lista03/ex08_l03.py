'''8. Dado um número inteiro N (N>0), verifique se o mesmo é primo.'''

n = int(input('Digite um número inteiro: '))
cont = 0

for i in range(1, n+1):
    if (n%i == 0):
        cont += 1

if cont == 2:
    print(f'{n} é primo.')
    
else:
    print(f'{n} não é primo.')
