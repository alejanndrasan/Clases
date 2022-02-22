#Ejercicio 5.6:

students = {
    "CI": {
        29954784:{
            "name":"Alejandra",
            "lastname": "Santos",
            "materias": [
                "algoritmos",
                "ingles",
                'matematica'
            ]
        }
    },
    "CI": {
        27893564:{
            "name":"Camila",
            "lastname": "Santos",
            "materias": [
                "algoritmos",
                "italiano",
                'matematica'
                ]
            }
        }   
    }

while True:
    option = input('''1. Agregar estudiante.
    \n 2. Eliminar estudiante.
    \n 3. Mostrar estudiantes registrados.
    \n 4. Salir.
    \n ==>  ''')
    #validacion:
    if option.isnumeric():
        option = int(option)
        if option < 1 and option>4:
            print("\nError, ingresa una opcion valida\n")
    else:
        print("\nError, ingresa una opcion valida\n")
    #Salir:
    if option == 4:
            print("Adios")
    #Agregar estudiante:
    if option == 1:
        #Nombre:
        while True:
            name = input("Inserta tu nombre: ")
            if name.isalpha():
                break
            else:
                print("Error. Ingresa un nombre valido")
    #Apellido:
        while True:
            apellido = input("Inserta tu apellido: ")
            if name.isalpha():
                break
            else:
                print("Error. Ingresa un apellido valido")
    #CI:
        while True:
            CI = input("Ingresa tu cedula: ")
            if CI.isnumeric():
                break
            else:
                print("Error. Ingresa un numero de cedula valido")
    #Materias:
        materias = []
        while True:
            materia = input("Ingresa la materia a inscribir: ")
            if materia.isalpha()==False:
                print("Error. Ingresa una materia valida")
                continue
            else:
                materias.append(materia)
            while True:
                op = input("Para agregar mas materias presiona 0, para finalizar presiona 1: " )
                
                    
    





                
                    





            


        
    




    

