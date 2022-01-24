#tarea 1: hacer una calculadora de numeros de mersenne

#inicio

num_n = 2
mersenne_num = 1
resultado = 1

def main():
    resultado = (2**num_n)-1
    print("The Mersenne number No.", str(mersenne_num), "is", str(resultado))
   

print("Welcome to the Mersenne calculator. \n")
answer = input("Would you like to calculate the first Mersenne number? (Yes or no) \n ==>")
if answer == "yes":
    main()

next_num = "yes"

while next_num: 
    next_num = input("Now, would you like to calculate the next Mersenne number? (Yes or No) \n ==>")
    if next_num == "yes":
        num_n += 1
        mersenne_num += 1
        main()
    else:
        break

print("See you later!")
