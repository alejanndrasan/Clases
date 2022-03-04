from tools import str_validation, intnum_validation, str_num_validation, floatnum_validation

class Student():
    def __init__(self, name, lastname, year, address, parent_name, parent_lastname, parent_number, grades, scholarship):
        self.name = name
        self.lastname = lastname
        self.year = year
        self.address = address
        self.parent_name = parent_name
        self.parent_lastname = parent_lastname
        self.parent_number = parent_number
        self.grades = grades
        self.scholarship = scholarship

    def show_database(self):
        print(f'''*****************************************
        \nNombre y apellido del Estudiante: {self.name} {self.lastname}
        \nGrado: {self.year}
        \nDireccion: {self.address}
        \nNombre y apellido del representante: {self.parent_name} {self.parent_lastname}
        \nNumero de telefono del representante: {self.parent_number}
        \nPromedio general: {self.grades}
        ''')
        if self.scholarship == True:
            print(f"\nPosee beca: Si")
        else:
            print(f"\nPosee beca: No")


        
        

