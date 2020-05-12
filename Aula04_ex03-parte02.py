def menu():
      print('Escolha a opção desejada: '
      '\n1- Ler idades'
      '\n2- Mostrar a media de idades'
      '\n3- Mostrar a quantidade de pessoas com idades abaixo da média'
      '\n4- Sair'
      '\n0- Exibir menu'
      '\n-----------------------------')

menu()

op = int(input('Digite a opção desejada: '))

lista_idades = []   #Lista onde serão adicionadas todas as idades

def evitar_div_por_zero():      #Evitar que o código realize divisão por 0 e quebre, caso o usuário digite a opção 2,4 como primeira opção/entrada
    if len(lista_idades) <= 0:
        lista_idades.append(0)

def funcao_programa_idades(): # Lita de opções para o usuário
    if op == 1:
        lista_idades.append(int(input(('Digite a idade: ')))) #Adcionar valor inteiro na lista
    elif op == 2:
        evitar_div_por_zero()
        media_idades = funcao_media_idades()
        print('A media entre as idades é: ', round(media_idades),'\nObs: A média será arredondada para o inteiro mais próximo\n')
    elif op == 3:
        evitar_div_por_zero()
        qtd_idades = 0 #Contador com a quantidade de posições na lista, referente a quantidade de idades digitadas pelo usuário
        media = funcao_media_idades() #Recebe a média de idades
        for i in range(len(lista_idades)): #Percore a lista
            if lista_idades[i] < media:
                qtd_idades += 1
        print('A quantidade de pessoas com idade abaixo da média é: ',qtd_idades,'\n')
    elif op == 0:
        print('\n-----------------------------')
        menu()
    else:
        print("Por favor digite uma das opções validas\n")

def funcao_media_idades():
    media_idades = 0
    for i in range(len(lista_idades)):
        media_idades += lista_idades[i]

    media_idades = media_idades / int(len(lista_idades))
    return media_idades

while op != 4:
    funcao_programa_idades()
    op = int(input('Digite a opção desejada: '))

print("Você escolheu sair do programa muito obrigado pela preferência ^.^")





