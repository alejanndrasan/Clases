veg = ["pimenton", "tofu", 'maiz']
car = ["jamon", 'salmon','pepperoni']

pizza = input('''Selecciona el tipo de pizza que deseas:
1. Vegetariana
2. Carne
==>  ''')

validacion = True

while validacion == True:
    if pizza.isnumeric and (pizza == "1" or pizza=="2"):
        validacion = False
    else:
        pizza = input('''caracter no valido,  el tipo de pizza que deseas:
1. Vegetariana
2. Carne
==>  ''')

pizza = int(pizza)

if pizza == 1:
    for x in veg:
        ingrediente = "2"
        while ingrediente == "2":
            print(x)
            ingrediente = input("Deseas este ingrediente en tu pizza? \n 1. Si \n 2. No")
            validacion = True
            while validacion == True:
                if ingrediente.isnumeric and (ingrediente == "1" or ingrediente=="2"):
                    validacion = False
                else:
                    ingrediente  = input("caracter no valido",  "Deseas", x, "en tu pizza? \n 1. Si \n 2. No")
            if ingrediente == "1":
                orden = ("Pizza con tomate, mozzarella y", x)

if pizza == 2:
    for x in car:
        ingrediente = "2"
        while ingrediente == "2":
            ingrediente = input("Deseas", x, "en tu pizza? \n 1. Si \n 2. No")
            validacion = True
            while validacion == True:
                if ingrediente.isnumeric and (ingrediente == "1" or ingrediente=="2"):
                    validacion = False
                else:
                    ingrediente  = input("caracter no valido",  "Deseas", x, "en tu pizza? \n 1. Si \n 2. No")
            if ingrediente == "1":
                orden = ("Pizza con tomate, mozzarella y", x)
