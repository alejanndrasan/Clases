vinyls = {
  '1': { 'name': 'Cuando Los Acéfalos Predominan',
        'author': 'Rawayana',
        'release_year': '2021',
        'stock': 1000,
        'sold': 0,
        'price': 10,
        },
  '2': { 'name': 'Notes on a Conditional Form',
        'author': 'The 1975',
        'release_year': '2020',
        'stock': 1200,
        'sold': 0,
        'price': 20,
      },
  '3': { 'name': 'Call Me If You Get Lost',
        'author': 'Tyler, the Creator',
        'release_year': '2021',
        'stock': 900,
        'sold': 0,
        'price': 30,
      },
  '4': { 'name': 'El Mal Querer',
        'author': 'Rosalía',
        'release_year': '2018',
        'stock': 980,
        'sold': 0,
        'price': 40,
      },
  '5': { 'name': 'The Dark Side of the Moon',
        'author': 'Pink Floyd',
        'release_year': '1973',
        'stock': 500,
        'sold': 0,
        'price': 50,
      },
}

'''Inventario:
Ver toda la información de todos los discos disponibles (no vale solo imprimir la estructura de datos que los tiene,
debe presentarse en consola de forma ordenada y legible)
Buscar información de un disco en específico por nombre'''

#Menu:
while True:
    opciones = input('''                    Bienvenido
    \nSeleccione la opcion que desea para continuar.
    \n1. Ver inventario completo.
    \n2. Buscar un disco.
    \n3. Registrar una venta.
    \n4. Ver todas las ventas realizadas.
    ==>  ''')
    if opciones.isnumeric() and 1<=int(opciones)<=4:
        opciones=int(opciones)
        break
    else:
        print("Error. Ingrese una opcion valida.")

#Inventario:

#Ver todos los vinilos disponibles:

if opciones==1:
    for key,value in vinyls.items():
        print(f'''{key}. {value['name']}:
        \nAutor: {value['author']}
        \nEstreno: {value['release_year']}
        \nIn Stock:{value['stock']}
        \nVendidos: {value['sold']}
        \nPrecio: {value['price']}\n''')

#Buscar vinilo:
if opciones==2:
    canciones = []
    for key in vinyls:
        canciones.append(vinyls[key]['name'])
    while True:
        print("Los albumes son los siguientes:", canciones)
        buscador = input('''Indique el nombre del album que desea: ''')
        if buscador.isprintable():
            buscador=buscador.upper()
            for cancion in canciones:
                if buscador == cancion:
                    for key, value in vinyls.items():
                        if cancion == {value['name']}:
                            print((f'''{key}. {value['name']}:
                        \nAutor: {value['author']}
                        \nEstreno: {value['release_year']}
                        \nIn Stock:{value['stock']}
                        \nVendidos: {value['sold']}
                        \nPrecio: {value['price']}\n''')) 

            
            #Por el numero:
            if buscador == 1:
                while True:
                    num = input('Ingrese el numero del album que busca: ')
                    if num.isnumeric():
                        break
                    else:
                        print("Error. Ingrese un nombre valido")
                for key, value in vinyls.items():
                    if {key} == num:
                        print(f'''{key}. {value['name']}:
                        \nAutor: {value['author']}
                        \nEstreno: {value['release_year']}
                        \nIn Stock:{value['stock']}
                        \nVendidos: {value['sold']}
                        \nPrecio: {value['price']}\n''')
                    elif {key} != num:
                        print("No se encuentra disponible. Puede buscar por otro parametro.")    
                #Por el nombre:
            if buscador == 2:
                while True:
                    name = input('Ingrese el nombre del album que busca:(sin espacios)\n==> ')
                    if name.isalpha():
                        break
                    else:
                        print("Error. Ingrese un nombre valido")
                for key, value in vinyls.items():
                    if {value['name']} == name:
                        print(f'''{key}. {value['name']}:
                        \nAutor: {value['author']}
                        \nEstreno: {value['release_year']}
                        \nIn Stock:{value['stock']}
                        \nVendidos: {value['sold']}
                        \nPrecio: {value['price']}\n''')
                    elif {value['name']} != name:
                        print("No se encuentra disponible. Puede buscar por otro parametro")
            break
        elif buscador.isnumeric():
            print("Error. Ingrese una opcion valida.")




