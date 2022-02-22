'''A. Dada una oración, escriba un programa Python para verificar si esa oración es un
Pangrama o no. Un pangrama es una oración que contiene todas las letras del alfabeto inglés.
(4 Puntos)
B. Decir cuántas letras se repiten en la oración original (4 Puntos)'''


'''pangrama = "El cadaver de Wamba, rey godo de Espana, fue exhumado y trasladado en una caja de zinc que peso un kilo"'''

import string


def pangrama_check(oracion, alfabeto, lista): 
    lista = []
    alfabeto = list(alfabeto)
    alfabeto.sort()  
            
    for x in oracion:
        x = x.lower()
        if x == ",":
            continue
        if x.strip():            
            lista.append(x)       

    lista = set(lista)
    lista = list(lista)
    lista.sort()

    if lista == alfabeto:
        print("La palabra es una pangrama")
    else:
        print("La palabra no es una pangrama")

def let_count(oracion, lista_letras, lista_rep):

    for i in oracion:
        if i.strip() in lista_letras:
            lista_rep.append(i)
        else:
            lista_letras.append(i)
    
    lista_rep = set(lista_rep)
    result = len(lista_rep)
    print(result)


def main():   
    let_list = []
    rep_list = []
    void_list = []
    alphabet = set(string.ascii_lowercase)
    phrase = input("Ingrese una oración para verificar que sea un pangrama \n==>")
    pangrama_check(phrase, alphabet, let_list)   
    let_count(phrase, let_list, rep_list)

main()
