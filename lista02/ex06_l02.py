'''06 - Dados dois números inteiros positivos i e j, imprimir em ordem crescente os N (lido) primeiros múltiplos de i ou de j ou de ambos.'''

i = int(input('i: '))
j = int(input('j: '))
n = int(input('n: '))
mi = i
mj = j

for cont in range(n):
    if mi < mj:
        print(mi)
        mi += i
    elif mi == mj:
        print(mi)
        mi += i
        mj += j
    else:
        print(mj)
        mj += j
