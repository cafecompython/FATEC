''' 10 - Dado um número inteiro em binário, o seu correspondente em decimal.
Ex.: 1011 (binário) -> 11 (decimal)'''

n = int(input('Digite um número em binário: '))

n_orig = n
potencia=0
rep=0
digito = 0

while n != 0:
    digito = n%10
    rep += digito * (2**potencia)
    n = n//10
    potencia += 1

print(f'O número binário {n_orig} em representação decimal é: {rep}')
    

