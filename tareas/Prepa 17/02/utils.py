def str_valid(msg1, msg2):
    while True:
        palabra = input(msg1) #palabra en este caso no toma ningun valor, lo que va a tomar el valor es el msg, con lo que pongamos como parametro al momemnto de ingresar la funcion
        if palabra.replace(" ",'').isalpha():
            break
        else:
            print(msg2)
    return palabra
def number_validation(msg1, msg2): #si paso dos parametros, arriba en dni tendria que poner dos parametros tambien
    while True:
        numero = input(msg1)
        if numero.isnumeric() and 0<int(numero):
            break
        else:
            print(msg2)
    return numero
def option_continue_validation(msg1, msg2):
    while True:
        numero = input(msg1)
        if numero.isnumeric() and 0<=int(numero)<=1:
            break
        else:
            print(msg2)
    return numero

def materias(msg):
    a_list = []
    while True:
        a = str_valid(msg, "Materia no valida. Ingrese otra vez")
        op=option_continue_validation('''\nDesea agregar otra materia:
        \n0. Si
        \n1. No''')
        op = int(op)
        a_list.append(a)
        if op == 2:
            break
    return a_list