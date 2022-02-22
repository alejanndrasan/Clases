from tools import *

def mostrar_estudiantes(e):
    for key, value in e.items():
        print(f'''\nCI: {key}:
        \nNombre: {value["Nombre"]} 
        \nApellido: {value["Apellido"]}
        \nAsignaturas: {value["Asignaturas"]}''')
