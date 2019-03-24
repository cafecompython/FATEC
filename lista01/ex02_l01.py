'''02 - Dados dois  números, imprima o maior (os dois números podem ser inteiros ou reais, cabe você a escolher). '''


num1 = int(input('Escreva o primeiro número: '))
num2 = int(input('Escreva o segundo número: '))

if num1 > num2:
    print(f'O maior número é {num1} e o menor é {num2}.')
elif num1 < num2:
    print(f'O maior número é {num2} e o menor é {num1}')
else: 
    print(f'Os números {num1} e {num2} são iguais.')

