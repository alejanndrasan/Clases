#31 de enero del 2022

#Ejercicio 1: n = primo1 * primo2

#1er paso, numeros primos:

''' def main():

    number_to_verify = input("Insert a number")
    
    if number_to_verify.isnumeric:
        isprime=True
        primelist = []
        resultadolist = []
        int(number_to_verify)
        aux = int(number_to_verify - 1)
        if number_to_verify == 1:
            isprime = False
        while aux > 1:
            isprime=True
            if number_to_verify % aux == 0:
                isprime=False
            if isprime:
                primelist.append(number_to_verify)
            aux-=1
        cont = 0
        cont2 = 1
        while cont < len(primelist):
            cont2 = cont + 1
            if len(resultadolist) > 0:
                print("The prime numbers are", resultadolist)
            while cont < len(primelist):
                resultado = primelist[cont] * primelist[cont2]
                break
                if resultado == number_to_verify:
                    resultadolist.append(cont)
                    resultadolist.append(cont2)
                    break
    else:
        number_to_verify = input("Not valid. Insert a number") '''

''' #Variables:  

num_n = ()
divider_list = []
prime_dividers = []
validation = False

#validacion:

validation=True
while validation:
    num_n = input("Insert a number: \n ==> ")
    if num_n.isnumeric():
        validation = False
    else:
        print("Not valid.")

num_n=int(num_n)

#Divisores:

for x in range(2, num_n):
    if num_n%x == 0:
        divider_list.append(x)
    print("All the dividers of the number", num_n, "are", divider_list)

#Divisores primos
    if '''





