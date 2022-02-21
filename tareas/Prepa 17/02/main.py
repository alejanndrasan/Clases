from modulo1 import *
from modulo3 import *


def main():
    db = {}
    print('\nBienvenido')
    while True:
        menu = number_validation('Ingresa: \n1.Ingreso de estudiante a la basa de datos. \n2.Para eliminar un estudiante de la base de datos. \n3.Para mostrar los estudiantes registrados en la base de datos. \n4. Editar a un estudiante registrado \n==>', "Ingresa una opcion valida")
        if int(menu) == 1:
            db = add_students(db)
            print(db)
        elif int(menu) == 2:
            pass
        elif int(menu) ==3:
            show_students(db)




main()