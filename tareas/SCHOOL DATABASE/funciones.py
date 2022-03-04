from tools import str_validation, intnum_validation, str_num_validation, floatnum_validation
from Students import Student

def registro(students):
    name = str_validation("\nIngrese el nombre del estudiante:  ", "\nIngrese un nombre valido")
    lastname = str_validation("\nIngrese el apellido del estudiante:  ", "\nIngrese un apellido valido")
    while True:
        year = intnum_validation("\nIngrese el grado del estudiante (1 - 11):  ", "\nIngrese un grado valido")
        if 1<= year <= 11:
            break
        else:
            print('\nIngrese un grado valido') 
    address = str_num_validation("\nIngrese su direccion:  ", '\nIngrese direccion valida')
    parent_name =  str_validation("\nIngrese el nombre del representante:  ", "\nIngrese un nombre valido")
    parent_lastname = str_validation("\nIngrese el apellido del representante:  ", "\nIngrese un apellido valido")
    parent_number = intnum_validation("\nIngrse el numero telefonico del representante: ", "\nIngrese un numero telefonico valido")
    while True:
        grades = floatnum_validation("\nIngrese el promedio general del estudiante: ", "Ingrese promedio valido")
        if 0<grades<=20:
            break
        else:
            print("Ingrese un promedio valido.")
    if grades >= 18:
        scholarship = True
    else:
        scholarship = False
    
    new_student = Student(name, lastname, year, address, parent_name, parent_lastname, parent_number, grades, scholarship)
    students.append(new_student)
    return students
        
def top2(students):
    students.sort(key = lambda student: student.grades, reverse=True)
    for i,student in enumerate(students):
        if i<2:
            print(student.show_database())



            

'''Cada alumno tiene nombre, grado que cursa, promedio, dirección de habitación, nombre del representante,
teléfono del representante y la condición de becado o no.
Si el promedio del alumno es menor a 18, el alumno no tendrá beca; de lo contrario, sí la tendrá.
Luego de almacenar esto en su base de datos, debe existir una función que permita ver la información organizada de cada alumno de la institución.
Como requerimientos adicionales pidieron:
Mostrar los nombres, grados  y promedios de las 5 personas con mejores promedios del colegio
Mostrar un promedio general de todos los promedios de los alumnos del plantel
Mostrar cuántos alumnos tienen promedios menores a 10, cuántos entre 10 y 15 (o sea, hasta 15.9) y cuántos entre 16 y 20.
'''