'''01 - Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Ex.: 210 é triangular, pois 5 x 6 x 7 = 210. Dado um numero natual, verifique se ele é triangular'''

num = int(input('Digite um número triangular: '))

i = 0

while (i*(i+1)*(i+2)) < num:
    i +=1

if (i*(i+1)*(i+2)) == num:
    print(f'Número triangular: {i} x {i+1} x {i+2} = {num}')
else:
    print(f'O número não é triangular.')

