#ejercicio 1:

''' num_n = input("Insert a three digit number: \n ==> ")

#validacion

validation = True
if num_n.isnumeric() and len(num_n)==3:
    validation = False
else: 
    num_n = input("Not valid. Insert a three digit number: \n ==> ")

if int(num_n[0])<int(num_n[1])<int(num_n[2]):
    print("SI")
else:
    print("NO") '''

#split: separa strings: 

''' cedulas = "2, 4, 5, 6"
lista_cedulas = cedulas.split()
print(lista_cedulas) # imprime las cedulas pero como lista 
cedula1 = cedulas.split()[0] '''

#Ejercicio 2:

A = [[1,4,6],[4,2,5],[6,5,3]]
B = []

escalar = input("Insert a number: \n ==>")
validation = True

while validation == True:
    if escalar.isnumeric():
        validation = False
    else: 
        escalar = input("Not valid. Insert a number: \n ==> ")
    

escalar = int(escalar)

for x in range(len(A)):
    r = []
    for y in (A[x]):
        r.append(y*escalar)
    B.append(r)
print(B)

    







