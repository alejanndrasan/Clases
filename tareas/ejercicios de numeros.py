#ejercicios de numeros:

#variables generales:

num_n = int(input("inserte un numero: "))
divisores_enteros = 0
primos_list = []
compuestos_list = []
oblongos_list = []
palindormo_list = []
perfectos_list = []
abundantes_list = []
deficientes_list = []
cuadrados_list = []

#primos
aux = num_n - 1
cont = 0
p_o_c = False

def primos(num_n):
    cont = 0
    if num_n == 1 :
        print("1 no es primo")
    else:
        for x in range(2, num_n):
            if num_n%x == 0:
                cont += 1
        if cont > 0:
            p_o_c = True
            print(num_n,"no es primo")
        else:
            print(num_n, "es primo")
            primos_list.append(num_n)

primos(num_n)

#compuestos:

def compuestos(num_n):
    if p_o_c == False and num_n != 1:
        print(num_n, 'es compuesto')
        compuestos_list.append(num_n)

compuestos(num_n)

#Oblongos:

def oblongos(num_n):
    for x in range(num_n):
        if x*(x+1) == num_n:
            print(num_n, 'es oblongo')
            oblongos_list.append(num_n)
    if oblongos_list == []:
        print(num_n, 'no es oblongo')

oblongos(num_n)

#palindromo:

def palindromos(num_n):
    num_str = str(num_n)
    if num_str == num_str[::-1]:
        palindormo_list.append(num_n)
        print(num_n, 'es palindromo')
    else:
        print(num_n, 'no es palindromo')

palindromos(num_n)

#perfectos:

def perfectos(num_n):
    divisores_enteros = 0
    for x in range(1, num_n):
        if num_n%x == 0:
            divisores_enteros+=x
    if divisores_enteros == num_n:
        print(num_n, 'es perfecto')
    else:
        print(num_n, 'no es perfecto')

perfectos(num_n)

#abundantes:

def abundantes(num_n):
    divisores_enteros = 0
    for x in range(1, num_n):
        if num_n%x == 0:
            divisores_enteros+=x
    if divisores_enteros > num_n:
        print(num_n, 'es abundante')
    else:
        print(num_n, 'no es abundante')

abundantes(num_n)

#deficientes:

def deficientes(num_n):
    divisores_enteros = 0
    for x in range(1, num_n):
        if num_n%x == 0:
            divisores_enteros+=x
    if divisores_enteros < num_n:
        print(num_n, 'es deficiente')
    else:
        print(num_n, 'no es deficiente')

deficientes(num_n)

#cuadrado

def cuadrados(num_n):
    for x in range(num_n):
        if x**2 == num_n:
            print(num_n, 'es un cuadrado')
            cuadrados_list.append(num_n)
    if cuadrados_list == []:
        print(num_n, 'es libre de cuadrados')
        

cuadrados(num_n)



    
    






