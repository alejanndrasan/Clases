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
s_f = 0
residuo = 0
num_8 = []

#Calculadora de numeros Fibonacci:

while sequence_f[-1] <= num_n:
    a_n = a_0 + a_1
    sequence_f.append(a_n)
    a_0 = a_1
    a_1 = a_n

s_f = len(sequence_f)
print(sequence_f)

check = False

for term in sequence_f:
    if term == num_n:
        print(term, "is in The Fibonacci Sequence.")
        check = True
        #Puesto en base 8:
        while cont <= (s_f - 2):
            cont += 1
        print(num_n, "is in the", "position", cont)
        if cont >= 8:
            while cont >= 1:
                residuo = cont%8
                num_8.append(residuo)
                cont = cont//8
            print(num_n,"is in the position","".join(map(str, num_8)),"in base 8.")


 
if check == False:
    print(num_n, "is not in The Fibonacci Sequence.")
    #Verificacion de si es primo:
    if num_n%2!=0:
        print(num_n, "is prime.")
    else:
        print(num_n, "is not prime.")