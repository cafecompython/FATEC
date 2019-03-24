'''01 - Faça um algoritmo que leia as informações dos alunos: MATRICULA, NOTA1, NOTA2, NOTA3, com o fim das informções indicado por MATRICULA=999. Para cada aluno, deve ser calculada a média de acordo com a seguinte fórmula: 

Média final = (2*NOTA1 + 3*NOTA2 + 4*NOTA3) / 9
Se média >= 7.0 => Imprima ‘APROVADO’, além da
MATRICULA e Média final.
Se média < 7.0 => Imprima ‘REPROVADO’, além da
MATRICULA e Média final.'''

mat = None

while mat != 999:
    mat = int(input('Digite sua matrícula ou "999" para encerrar: '))
    if mat != 999:
        nota1 = int(input('Digite sua primeira nota: '))
        nota2 = int(input('Digite sua segunda nota: '))
        nota3 = int(input('Digite sua terceira nota: '))

        media_final = (2*nota1 + 3*nota2 + 4*nota3)/9
        if media_final >= 7.0:
            print(f'Aprovado. Matrícula: {mat}; Média final: {media_final}.')
        else:
            print(f'Reprovado. Matrícula: {mat}; Média final: {media_final}')
    else:
        print('Programa encerrado')
