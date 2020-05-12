i = 0
media_altura = 0
maior_altura = ['Nome',0.00]
menor_altura = ['Nome',3.00]

while i < 10:
    nome = input('Digite o nome dx {}º alunx: '.format(i+1))
    altura = float(input(('Digite a altura dx {}: '.format(nome))))
    media_altura += altura

    if altura > maior_altura[1]:
        maior_altura[0] = nome
        maior_altura[1] = altura

    if altura < menor_altura[1]:
        menor_altura[0] = nome
        menor_altura[1] = altura
    i += 1

media_altura = media_altura/10

print('\n-------------------------------------\n')
print('A media entre os alunxs é {:.2f}m:'.format(media_altura))
print('A maior altura é dx {} em {}m'.format(maior_altura[0],maior_altura[1]))
print('A menor altura é dx {} em {}m'.format(menor_altura[0],menor_altura[1]))


