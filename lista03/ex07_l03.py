'''07 - Dados três números inteiros positivos, verifique se eles formam os lados de um triângulo retângulo.'''

hip = int(input('Digite o primeiro número: '))
lado1 = int(input('Digite o segundo número: '))
lado2 = int(input('Digite o terceiro número: '))

if ((lado1*lado1 + lado2*lado2) == (hip*hip)) or ((hip*hip + lado2*lado2) == (lado1*lado1)) or ((lado1*lado1 + hip*hip) == (lado2*lado2)):
    print(f'Os números {hip}, {lado1} e {lado2} são lados de um triângulo retângulo.')
else: 
    print(f'Os números {hip}, {lado1} e {lado2} não são lados de um triângulo retângulo.')
