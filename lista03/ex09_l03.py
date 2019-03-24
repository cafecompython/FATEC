'''09 - Dado um número inteiro N (N>0), determinar se seus dígitos estão em ordem estritamente crescente.

N=341 => não
N=2457 => sim
N=335 => não '''


n_o = int(input('Digite um número: '))
n = n_o
dmd = n%10
n = n//10

while n != 0 and (n%10 < dmd):
    dmd = n%10
    n = n //10

if n == 0:
    print(f'Os dígitos de  {n_o} são estritamente crescentes')
else:
    print(f'Os dígitos de  {n_o} não são estritamente crescentes')

