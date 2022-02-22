# 7 de febrero de 2022

#numero malvados:

def even_ones(numero_n_binario):
    cont = 0
    for x in numero_n_binario:
        if x == 1:
            cont += 1

    return is_even(cont)

def is_even(cont):
    if cont >= 1:
        

def numero_binario(num_n):

    num_n_binario = []
    aux = num_n
    while aux >= 2:
        num_n_binario.append(aux % 2)
        if aux == 2:
            num_n_binario.append(aux // 2)
        aux //= 2
    num_n_binario.reverse()
    return num_n_binario


def numero_malvado():
    num_n = int(input("Insert a number:  "))
    numero_n_binario = numero_binario(num_n)
    is_even = even_ones(numero_n_binario)