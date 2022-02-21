def show_students(h):
    for dni, students in h.items():
        print(f'''\nCedula {dni}\n Nombre: {students['name']}\nApellido {students['lastName']}''')
    print('Materias:')
    for materia in students['Asignaturas']:
        print(materia)