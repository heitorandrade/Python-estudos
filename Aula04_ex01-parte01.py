item = 0

lista_produtos = []

while item < 50:                                                                 #loop para inserir 50  valores de itens na lista_produtos
    valor = float(input('Digite o preço do produto de ID {}: '.format(item+1)))  #Armazena o valor em float do item
    lista_produtos.append(valor)                                                 #Adiciona cada item a uma posição da lista
    item += 1

print(
      '\n\nTabela de preços da Lojas Quase Dois'
      '\n------------------------------------'
      )

for i in range(50):                                                       #loop para exibir a lista de produtos com os respectivos valores
    print("ID: {:} | R$ {:.2f} ".format(i+1,lista_produtos[i]))

