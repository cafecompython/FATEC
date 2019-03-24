'''10 - Dada uma sequência de letras terminadas pelo caracter Z, imprima a quantidade de vogais.'''

lista_char = input('Digite uma letra ou "Z" para terminar: ')

letra = ''
cont = 1
vogais = 'aeiou'
lista_vogais = ''

if lista_char in vogais:
    cont_vogais = 1
    lista_vogais += lista_char
else:
    cont_vogais = 0


if lista_char != 'Z':

    while letra != 'Z':
        letra = input('Digite outra letra ou "Z" para terminar: ')
        lista_char += letra
        cont +=1

        if letra in lista_vogais:
            cont_vogais += 1
            lista_vogais += letra

print(f'Letras digitadas: "{lista_char}"')
print(f'Quantidade de letras digitadas: {cont}')

print(f'Vogais digitadas: "{lista_vogais}"')
print(f'Quantidade de vogais digitadas: "{cont_vogais}"')
