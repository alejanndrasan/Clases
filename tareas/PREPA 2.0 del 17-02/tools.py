#validador de palabras:
def word_valid(msg1, msg2):
    while True:
        word = input(msg1)
        if word.replace(" ", "").isalpha():
            break
        else:
            print(msg2)
    return word

#validador de palabras:
def num_valid(msg1, msg2):
    while True:
        num = input(msg1)
        if num.isnumeric():
            num = int(num)
            if num>0:
                break
        else:
            print(msg2)
    return num

#listas:
def list_maker(msg1, msg2):
    list_n = []
    while True:
        element = word_valid(msg1, msg2)
        while True:
            op = num_valid('''\nIngrese 1 para agregar mas elementos, ingrese 2 para finalizar:
            \n==>  ''', "\nIngrese opcion valida.")
            if 1<=int(op)<=2:
                op = int(op)
                break
            else:
                print("Ingrese opcion valida.")
        list_n.append(element)
        if op == 2:
            break
    return list_n



