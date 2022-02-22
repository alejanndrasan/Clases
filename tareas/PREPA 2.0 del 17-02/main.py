from tools import num_valid
from modulo1 import *
from modulo3 import *

def menu():
    db = {}
    while True:
        while True:
            opciones_menu = num_valid('''\n************* Bienvenid@ ***************
            \nSeleccione la opcion que desea realizar:
            \n1. Registrar estudiante.
            \n2. No se.
            \n3. Mostrar estudiantes registrados.
            \n4. Salir 
            \n==> ''', "Ingrese caracter valido")
            if 1<= opciones_menu <= 4:
                break
            else:
                print("Ingresa opcion valida.")
        if opciones_menu == 1:
            db = registro(db)
            continue
        if opciones_menu == 2:
            print("No se")
            continue
        if opciones_menu ==3:
            mostrar_estudiantes(db)
            continue
        if opciones_menu == 4:
            print("Chaooo")
            break
        
        







menu()
