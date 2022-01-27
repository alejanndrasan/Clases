#descargar synth wave

# BUCLE FOR:

#for x in range(5): #se recorre por cada numero del rango sin incluir el extremo derecho
    #print(x)

#print("\n----------------------")

#for x in range(1,5): #ahora inicia en 1, no en el default, cero.
    #print(x)

#print("\n----------------------")

#for x in range(1, 5, 2): #ahora inicia en 1, termina en cuatro y va de dos en dos.
    #print(x)

#print("\n----------------------")

#for x in [1,2,3,4,5,6]: #ahora recorre cada elemento de la lista sin excluir el extremo derecho
    #print(x)

#print("\n----------------------")

#for x in ["ale", 'luis', 'miguel']: #recorre los elementos igual
    #print(x)

#print("\n----------------------")

#for x in [["ale", 20], 'luis', 'miguel']: #recorre los elementos igual
    #print(x)

#print("\n----------------------")

#estudiantes = ['rommel', 'miguel', 'ale']
#for x in estudiantes: #es lo mismo que los ultimos dos ejemplos
    #print(x)

#print("\n----------------------")

#for x in range(len(estudiantes)):
    #print(x)

#print("\n----------------------")

# BUCLE WHILE:

#x=0
#while x<5: 
    #print(x)
    #x+=1

#option = 0
#while option == 0:
    #option = int(input(''' Ingresa 0 para seguir en el menu, 
    #ingresa otro numero para salir: \n==>'''))
#las tres comillas es para strings largos

# EJERCICIO 1:

'''
print("Bienvenido a la calculadora de numeros perfectos.\n")

def main():
    flag_num = True #validacion
    while flag_num: 
        num_to_verify = input("Ingresa un numero: ")
        if num_to_verify.isnumeric():
            flag_num = False
        else:
            print("El numero introducido no es valido \n")

    num_to_verify = int(num_to_verify)

    suma = 0
    for x in range(1, (num_to_verify//2)+1):
        if num_to_verify % x == 0:
            suma += x
    
    if suma == num_to_verify: 
        print("El numero", str(num_to_verify), "es perfecto.")
    else:
        print("El numero", str(num_to_verify), "no es perfecto")
    
    pregunta = (input("Para calcular otro numero, ingresa 0, ingresa cualquier otro caracter para salir: \n ==> "))
    if pregunta == "0":
        return main()
    else:
        print("Chaooo <3")

main()
'''

# EJERCICIO 2.3 codigo morse

codigo_postales = "...._ __... ..... ..___ * .____ ___.. ___.. _____" #4752 y #1880
codigo = ''
numero0 = ''

for index in range(len(codigo_postales)):
    if codigo_postales[index] != '' and codigo_postales[index] != '*':
        codigo += codigo_postales[index]
 #haces la representacion de la tabla 

 






    





    


    









