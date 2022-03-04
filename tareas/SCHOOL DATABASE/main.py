from tools import intnum_validation, str_validation, str_num_validation, floatnum_validation
from Students import Student
from funciones import registro, top2



'''Cada alumno tiene nombre, grado que cursa, promedio, dirección de habitación, nombre del representante,
teléfono del representante y la condición de becado o no.
Si el promedio del alumno es menor a 18, el alumno no tendrá beca; de lo contrario, sí la tendrá.
Luego de almacenar esto en su base de datos, debe existir una función que permita ver la información organizada de cada alumno de la institución.
Como requerimientos adicionales pidieron:
Mostrar los nombres, grados  y promedios de las 5 personas con mejores promedios del colegio
Mostrar un promedio general de todos los promedios de los alumnos del plantel
Mostrar cuántos alumnos tienen promedios menores a 10, cuántos entre 10 y 15 (o sea, hasta 15.9) y cuántos entre 16 y 20.
'''
def main():
    students = []
    while True:
        while True: 
            menu = intnum_validation('''\n******************** Bienvenido ******************************
            \nSelecciona una opcion:
            \n1. Registrar estudiante.
            \n2. Motrar base de datos de los estudiantes.
            \n3. Mostrar top 5 mejores estudiantes.
            \n4. Mostrar promedio general.
            \n5. Mostrar cantidad de estudiantes por promedio.
            \n6. Salir.
            \n ==>   ''', 'Ingrese un caracter valido')
            if 1<= menu <= 6:
                break
            else:
                print("Igrese una opcion valida")
        if menu ==1:
            registro(students)
        elif menu ==2:
            for i in students:
                print()
                i.show_database()
        elif menu == 3:
            top2(students)
        elif menu==6:
            print("Hasta luego!")
            break
        
        
                
    


main()


