'''09 - Dada uma sequência de letras terminadas pelo caracter Z, imprima a quantidade de caracteres digitados.'''

lista_char = input('Digite uma letra ou "Z" para terminar: ')

letra = ''
cont = 1

if lista_char != 'Z':

    while letra != 'Z':
        letra = input('Digite outra letra ou "Z" para terminar: ')
        lista_char += letra
        cont +=1

print(f'Letras digitadas: "{lista_char}"')
print(f'Quantidade de letras digitadas: {cont}')
