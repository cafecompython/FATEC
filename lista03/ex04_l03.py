'''04 - Dada uma seqüência de caracteres terminada pelo caracter ponto (‘.’). Imprima cada caracter lido eliminando os espaços. Obs.: cada
dois ou mais espaços consecutivos deverá ser impresso apenas um espaço.'''


char_io = input('Digite um caracter: ')


final = char_io
char_ant = ''
cont = 0

while char_io != '.':
    char_io = input('Digite outro character ou "." para encerrar: ')

    if char_io == ' ':
        char_ant = char_io
        char_io = ''
        cont += 1
        if cont > 1:
            char_io= ' '
            final +=  char_io
            cont = 0
        else:
            final += char_io
    else:
        final+= char_io


print(final)
