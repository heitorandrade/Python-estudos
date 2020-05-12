contador = 0
soma_par = 0
soma_impar = 0

while contador <= 20:
    if contador % 2 == 0:
        soma_par = soma_par + contador
    else:
        soma_impar = soma_impar + contador
    contador = contador + 1

print("soma dos pares: ",soma_par,"\nsoma dos impares: ",soma_impar)
