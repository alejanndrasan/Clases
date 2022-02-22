'''Dos números amigos son dos números enteros positivos a y b tales que la 
suma de los divisores propios de uno es igual al otro número y viceversa,
es decir σ(a)=b y σ(b)=a, donde σ(n) es igual a la suma de los divisores de n,
sin incluir a n.'''

def amigos():
    while True:
        num_n = input("Insert a number: ")
        num_m =input("Insert another number: ")
        if num_m.isnumeric() and num_n.isnumeric():
            num_n=int(num_n)
            num_m=int(num_m)
            break
        else:
            print("Insert a valid number")
    divisores_n = divisores(num_n)
    divisores_m = divisores(num_m)
    if divisores_n == num_m and divisores_m == num_n:
        print("The numbers", num_n, "and", num_m, "are friends")
    else:
        print("The numbers", num_n, "and", num_m, "are not friends")

def divisores(number):
    suma = 0
    for x in range(1, number):
        if number%x==0:
            suma+=x
    return suma
            

amigos()




        

