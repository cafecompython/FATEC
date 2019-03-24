'''5. Dada uma série 1, -1/2, 1/3, -1/4, 1/5, ... imprima os 10 primeiros termos, bem como a soma dos mesmos. '''


signal = 1
soma = 0

for i in range(1,11):
    termo = signal/i
    soma += termo
    signal = -signal
    print(termo)

print(soma)
