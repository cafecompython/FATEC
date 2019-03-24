'''07 -Dada uma lista de números reais terminada pelo número 99,99, imprima cada número lido. No final, imprima a média aritmética de todos os números da lista (é calro que o 99,99 não faz parte da média).'''

N = float(input('Digite um número: '))
soma = 0
cont = 1
while N != 99.99:
    print(N)
    soma += N
    cont +=1
    N = float(input('Digite outro número, ou 99.99 para encerrar: '))
media = soma/(cont-1)
print(f'A média aritmética dos números digitados é: {soma}/{cont-1} = {media}')
