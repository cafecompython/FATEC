'''06 - Dado um número inteiro N, divida-o por 2 (sucessivamente)
enquanto o resultado for maior que 0. No final, imprima o número de divisões necessárias para zerar o quociente.'''

N = int(input('Digite um número inteiro: '))
i = 0
while N > 0:
    N = N//2
    print(N)
    i += 1
print(i)
