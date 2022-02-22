''' Datos que deben insertarse:
1. CI
2. Nombre
3. Apellido
4. Asignaturas
'''

estudiantes = {
    29876567:{
        "nombre":"Alejandra",
        "apellido": "Santos",
        "asignaturas": [
            "MatematicaV"
            "InglesVI"
            "Algoritmos"
        ]
    }
}

while True:
    opcion = input('''                BIENVENIDO\n
           Por favor seleccione una opcion: \n
           1. Inscribir estudiante. \n
           2. Eliminar estudiante. \n
           3. Ver estudiantes inscritos.
           4. Salir.
           \n==>  ''')
    if opcion.isnumeric():
        opcion=int(opcion) 
        

