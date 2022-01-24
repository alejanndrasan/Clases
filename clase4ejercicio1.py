print("Welcome to the calculator!")
print("note: just enter absolute values.")

def main():
    operacion = int(input("Select the operation: \n 1. Addition. \n 2. Subtraction. \n 3. Multiply \n 4. Divide. \n ==>"))
    if operacion == 1:
        num1 = float(input("Insert 1 number: "))
        num2 = float(input("Insert 1 number: "))
        resultado = num1 + num2
        print("Your result is: ", str(resultado))
        repeticion = input("Would you like to make another operation? (Yes or No) \n ==>")
        if repeticion == "yes":
            return main() 
        else:
            print("See ya!")
    elif operacion == 2:
        num1 = float(input("Insert 1 number: "))
        num2 = float(input("Insert 1 number: "))
        resultado = num1 - num2
        print("Your result is: ", str(resultado))
        repeticion = input("Would you like to make another operation? (Yes or No) \n ==>")
        if repeticion == "yes":
            return main() 
        else:
            print("See ya!")
    elif operacion == 3:
        num1 = float(input("Insert 1 number: "))
        num2 = float(input("Insert 1 number: "))
        resultado = num1 * num2
        print("Your result is: ", str(resultado))
        repeticion = input("Would you like to make another operation? (Yes or No) \n ==>")
        if repeticion == "yes":
            return main() 
        else:
            print("See ya!")
    elif operacion == 4:
        num1 = float(input("Insert 1 number: "))
        num2 = float(input("Insert 1 number: "))
        resultado = num1 * num2
        print("Your result is: ", str(resultado))
        repeticion = input("Would you like to make another operation? (Yes or No) \n ==>")
        if repeticion == "yes":
            return main() 
        else:
            print("See ya!")
    else:
        print("The character you entered is invalid.")
        return main()
main()

    