'''06 - Dada uma seqüência de N números inteiros, determinar o tamanho da maior subseqüência.'''

entrada = int(input("Digite quantos números deseja digitar: "))
cont = 0
maior = 1
digito_anterior = None

for i in range(entrada):
    digito = int(input('Digite o primeiro número: '))
    if digito_anterior == digito:
        cont += 1
        maior = cont
    else:
        cont = 1
    digito_anterior = digito

print(f'Maior subsequência = {maior}')
