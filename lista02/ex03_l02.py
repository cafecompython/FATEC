'''03 - Dada a sequência abaixo, calcular {a}'''

denominador = 50
alfa = 0

for expoente in range(1,51):
    print, denominador
    alfa += (2**expoente/(denominador))
    denominador -= 1

print(alfa)
