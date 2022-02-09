''' #Estrutucturas combinadas:
    #se pueden poner diccionarios en diccionarios, listas en listas, diccionarios en listas, etc.

secciones = [["jose", 'ana','andres'], ['luis', 'maria', 'pedro']]

for i in range(len(secciones)): #len es 2, y range pasa de 0 a 1
    for j in range(len(secciones[i])):
        print("el nombre del estudiante es: {} ".format(secciones[i][j])) #el format sigue orden de llegda
'''

#Ejercicio: meyer.

#la serie fibonacci inicia en 0 y es la suma de cada termino de la serie.


num_n = (input("Insert a number to check if is in The Fibonacci Sequence: \n ==>  "))

#Validacion:

validacion = False
while validacion == False: 
    if num_n.isnumeric():
        num_n = int(num_n)
        validacion = True
    else:
        num_n = (input("Not valid. Insert a number to check if is in The Fibonacci Sequence: \n ==>  "))
    

#Variables:

a_0 = 0
a_1 = 1
a_n = 0
cont = 0
sequence_f = [a_0, a_1]

#Calculadora de numeros Fibonacci:

while sequence_f[-1] <= num_n:
    a_n = a_0 + a_1
    sequence_f.append(a_n)
    a_0 = a_1
    a_1 = a_n

print(sequence_f)

check = False

for term in sequence_f:
    if term == num_n:
        print(term, "is in The Fibonacci Sequence.")
        check = True
 
if check == False:
    print(num_n, "is not in The Fibonacci Sequence.")

















        


        








