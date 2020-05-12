i = 0
soma_altura = 0

while i < 10:
    soma_altura += float(input('Digite a idade a altura da {}º pessoa: '.format(i+1)))
    i += 1

print('A média das alturas é',round(soma_altura/10,2),'m')