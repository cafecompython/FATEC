'''02 - Dados dois números inteiros positivos x e y, fazer a divisão de x por y sem usar o operador de divisão.'''

x = int(input('Forneça o primeiro número: '))
y = int(input('Forneça o segundo número: '))

cont = 0
while x >= 0:
    x-=y
    cont+=1

print(cont-1)

