from tools import *

def registro(e):
    ci=num_valid("\nInserte el numero de cedula del estudiante: ", "\nIngrese un numero de cedula valido.")
    nombre = word_valid("\nIngrese su nombre: ", "\nIngrese un nombre valido.")
    apellido = word_valid("\nIngrese su apellido: ","\nIngrese un apellido valido." )
    materias = list_maker("\nIngrese una materia: ", "\nINgrese materia valida.")
    e[ci]={
        "Nombre": nombre,
        "Apellido": apellido,
        "Asignaturas": materias
    }
    return e