#31 de enero de 2022

#Ejrecicio 2:

#Variables:

idcard =()
age = ()
gender = ()
study_type = ()
studies = {"U": 8900, "T": 12000, "L": 7000}
payment = 0
study = ()
costumer_count = 0
u_study_count = 0
t_study_count = 0
l_study_count = 0
total_discount = 0
acum__total = 0
want_to_exit = False
acum_u = 0
acum_t = 0
acum_l = 0


def main():

    while want_to_exit == False:
    
        print("Welcome")
        idcard=input("Enter your ID: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")
        study_type = input("Enter the study you're going to have: ")
        payment=[str(studies[study_type.upper()])]
        costumer_count += 1
        amount = payment

        #femenino y mayor a 55 o masculino y mayor de 65:

        if (gender.lower() == "f" and age >= 55) or (gender.lower()=="m"and age >= 65):
            
            payment *= 0.75
            print("ID:", idcard)
            print("Age:", age)
            print("Gender:", gender)
            print("Study:", study_type)
            print(str(payment))
            total_discount += amount*.25 #se le suma lo descontado
        
        #si es impar, descuento del 20%:

        if costumer_count %2 != 0:
            payment -= amount * 0.02
            total_discount += amount*.02 #se le suma lo descontado

        #cantidad de clientes por tipo de estudio

        if study_type.upper == "U":
            u_study_count += 1
            acum_u += payment
        elif study_type.upper == "T":
            t_study_count += 1
            acum_t += payment
        elif study_type.upper == "L":
            l_study_count += 1
            acum_l += payment
        
        #monto neto:
        acum__total += payment

        contin = input('Would you like to continue. \n 1. Continue. \n 2.Exit' )
        if contin == "1":
            return main()
        elif contin == "2":
            want_to_exit = True

# ahora imprimir todo, arreglar los detalles.


    


    
    
main()

        

        

