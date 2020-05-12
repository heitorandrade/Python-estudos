n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
n3 = float(input('Digite a 3º nota: '))
n4 = float(input('Digite a 4º nota: '))

media = (n1 + n2 + n3 + n4)/ 4

if(media>=5):
    print('O aluno passou de ano. \nA Média é: {:.2f}'.format(media))
else:
    print('O aluno foi reprovado. \nA média é: {:.2f}'.format(media))
