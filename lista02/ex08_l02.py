'''08 - Dado um número inteiro decimal (base 10), imprimir seu correspondente em binário (divisões sucessivas).'''

n0 = int(input('Digite um número inteiro decimal: '))

rep = 0
d = 1
n=n0
while n != 0:
    binario = n%2
    digito = binario*d
    rep += digito
    n = n//2
    d=d*10
print(f'{n0} em binário é: {rep}')
