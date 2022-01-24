def main():
    variable = "hola"
    variable2 = "unimetanos"
    print(variable, variable2, sep="") #con la coma se pone un espacio entre variables
    v3 = "hola"
    v4 = "antonio"
    v5 = "{1} {0}".format(v3,v4) #toma 0 como v3 y 1 como v4
    print(v5)
    
def main2(): #ejercicio 3
    print("welcome to the prime calculator")
    num_to_verify = int(input("please enter a number"))
    aux = num_to_verify - 1
    cont = 0

    while aux > 1: 
        if num_to_verify % aux == 0: 
            cont += 1
        aux -=1
        

    if cont == 0:
        print ("the number to verify is prime")
    else:
        print('the number is not prime')







main2()