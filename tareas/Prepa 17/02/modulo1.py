from utils import *

def add_students(db):
    name = str_valid('Ingresa el nombre del estudiante: ','Ingreso Invalido. Ingrese nuevamente su nombre: ')
    last_name =str_valid('Ingresa el apellido del estudiante: ','Ingreso Invalido. Ingrese nuevamente su apellido: ')
    dni = number_validation('Ingrese su cedula: ','Ingreso Invalido. Porfavor ingresa tu cedula: ')
    asignaturas = []
    option = 0
    while option == 0:    
        option = option_continue_validation('Ingrese 0 si desea continuar o ingrese 1 si desea salir: ','Ingreso Invalido. Por favor ingres 0 para continuar o 1 para salir: ')
        db[dni] = {'name':name , 'lastName':last_name, 'Asignaturas':asignaturas }
        option=int(option)
    return db

add_students()