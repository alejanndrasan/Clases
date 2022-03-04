#Expreso saman:

'''a) Para cada cliente, el programa deberá desplegar la información del recibo con los
siguientes datos:
- El número de cédula de identidad del cliente
- Cantidad de pasajeros
- Código y nombre del destino solicitado
- Monto bruto a pagar
- Monto de descuento (si no aplica, el programa mostrará cero)
- Monto del impuesto a pagar (IVA 16% del monto bruto menos el descuento)
- Monto neto a pagar'''

'''b) Al final del día:
- La cantidad de clientes por destino (no pasajeros)
- El Monto Total Neto Facturado por destino
- El Monto Total de Descuentos otorgados por destino
- El Monto Total Neto Facturado por Expresos Saman
- Los datos del cliente que más dinero pagó'''

import string

clientes = []
monto_total_V = 0
monto_total_P = 0
monto_total_B = 0

def menu():

    destinos = {
        "V": {
            "nombre": "Valencia",
            "precio": 500,
            "puestos": 30
        },
        "P":{
            "nombre": "Puerto La Cruz",
            "precio": 700,
            "puestos": 30
        },
        "B":{
            "nombre": "Barquisimeto",
            "precio": 800,
            "puestos": 30
        }
    }
    while True:
        
        while True:
            menu_bienvenida = input('''\n*********************** Bienvenido al Expreso Saman *****************************
            \n1. Comprar boletos.
            \n2. Ver la cantidad de clientes por destino (no pasajeros).
            \n3. El Monto Total Neto Facturado por destino
            \n4. El Monto Total de Descuentos otorgados por destino
            \n4. El Monto Total Neto Facturado por Expresos Saman
            \n5. Los datos del cliente que más dinero pagó 
            \n6. Salir.
            \n==> ''')
            #Validacion:
            if menu_bienvenida.isnumeric() and (int(menu_bienvenida)==1 or int(menu_bienvenida)==2 or int(menu_bienvenida)==3 or int(menu_bienvenida)==4 or int(menu_bienvenida)==5 or int(menu_bienvenida)==6):
                menu_bienvenida = int(menu_bienvenida)
                break
            else:
                print("\nInserte una opcion valida")
        if menu_bienvenida == 1:
            comprar_boletos(destinos, clientes, monto_total_V, monto_total_P, monto_total_B)
        if menu_bienvenida == 3:
            monto_total_D(monto_total_V, monto_total_P, monto_total_B)
        if menu_bienvenida == 6:
            print("\nHasta luego")
            break
        
        
def comprar_boletos(destinos, clientes, monto_total_V, monto_total_P, monto_total_B):


    for codigo, datos in destinos.items():
        print(f'''\n****************** Codigo del destino: {codigo} ***************************
        \nDestino: {datos["nombre"]}
        \nPrecio: {datos["precio"]}
        \nPuestos disponibles: {datos["puestos"]}''')

    #Registro del pedido:

    #Cedula:
    while True:
        cedula = input("\nCI: ")
        if cedula.isnumeric():
            break
        else:
            print("\nInserta un numero de CI valido.")

    #Codigo del destino:
    while True:
        codigo_n = input("\nCodigo del destino: ")
        codigo_n.strip() 
        if codigo_n.isalpha() and (codigo_n.upper()=="V" or codigo_n.upper()=="P" or codigo_n.upper()=="B"):
                break
        else:
            print("\nInserta un codigo valido.")

    #Numero de puestos:
    for codigo, datos in destinos.items():
        print(f'''\nPara el destino codigo {codigo} hay {datos["puestos"]} puestos''')

    #Puestos para V:
    if codigo_n == "V":               
        while True:
            pasajeros = input("\nNumero de Puestos: ")
            if pasajeros.isnumeric() and int(pasajeros)>0:
                pasajeros = int(pasajeros)
                if pasajeros > destinos["V"]["puestos"]:
                    print("\nNumero de puestos no disponibles.")
                elif pasajeros <= destinos["V"]["puestos"]:
                    destinos["V"]["puestos"] -= pasajeros
                    break
            else:
                print("\nInserta un numero de puestos valido.")

    #Puestos para P:
    if codigo_n == "P":               
        while True:
            pasajeros = input("\nNumero de Puestos: ")
            if pasajeros.isnumeric() and int(pasajeros)>0:
                pasajeros = int(pasajeros)
                if pasajeros > destinos["P"]["puestos"]:
                    print("\nNumero de puestos no disponibles.")
                elif pasajeros <= destinos["P"]["puestos"]:
                    destinos["P"]["puestos"] -= pasajeros
                    break
            else:
                print("\nInserta un numero de puestos valido.")

    #Puestos para B:
    if codigo_n == "B":               
        while True:
            pasajeros = input("\nNumero de Puestos: ")
            if pasajeros.isnumeric() and int(pasajeros)>0:
                pasajeros = int(pasajeros)
                if pasajeros > destinos["B"]["puestos"]:
                    print("\nNumero de puestos no disponibles.")
                elif pasajeros <= destinos["B"]["puestos"]:
                    destinos["B"]["puestos"] -= pasajeros
                    break
            else:
                print("\nInserta un numero de puestos valido.")

    #Monto bruto:
    monto_bruto = 0
    if codigo_n == "V":
        monto_bruto = pasajeros * destinos["V"]["precio"]
    if codigo_n == "P":
        monto_bruto = pasajeros * destinos["P"]["precio"]
    if codigo_n == "B":
        monto_bruto = pasajeros * destinos["B"]["precio"]
    
    #IVA:
    IVA = monto_bruto * 0.16
    monto_IVA = monto_bruto + IVA

    #Monto con descuento:
    if pasajeros >=  4:
        descuento = monto_IVA * 0.20
        monto_neto = monto_IVA - descuento
    else:
        descuento = 0
        monto_neto = monto_IVA
    
    #monto neto por destino:
    if codigo_n == "V":
        monto_total_V += monto_neto
        print(monto_total_V)
    if codigo_n == "P":
        monto_total_P += monto_neto
        print(monto_total_P)
    if codigo_n == "B":
        monto_total_B += monto_neto
        print(monto_total_B)

    
    cliente = {
        "CI": cedula,
        "Codigo del Destino": codigo_n,
        "Numero de puestos": pasajeros,
        "Monto a cancelar": monto_neto
    }
    clientes.append(cliente)
    factura(cedula, codigo_n, pasajeros, monto_bruto, IVA, descuento, monto_neto)

def factura(ci, cod, puestos, monto_b, i, desc, monto_n ):
    print(f'''\n************* Factura ****************
    \nCI: {ci}
    \nCodigo del destino: {cod}
    \nNumero de puestos: {puestos}
    \nMonto bruto: {monto_b}
    \nIVA: {i} 
    \nDescuento (para compras de 4 pasajeros en adelante): {desc}
    \nMonto total a cancelar: {monto_n}''')

def monto_total_D(monto_total_V, monto_total_P, monto_total_B):

    while True:
        cod_dest = input('''\n********** Inserte el codigo del destino que desea visualizar ******************
        \n V: Valencia.
        \n P: Puerto la Cruz.
        \n B: Barquisimeto.
        \n ===>  ''')
        cod_dest.strip() 
        if cod_dest.isalpha() and (cod_dest.upper()=="V" or cod_dest.upper()=="P" or cod_dest.upper()=="B"):
             break
        else:
            print("\nInserta un codigo valido.")
    
    #Total neto facturado para V:
    if cod_dest == "V":               
        print(f"\nEl monto neto total facturado del destino {cod_dest} es {monto_total_V}")
    
    #Total neto facturado para P:
    if cod_dest == "P":               
        print(f"\nEl monto neto total facturado del destino {cod_dest} es {monto_total_P}")

    #Total neto facturado para B:
    if cod_dest == "B":               
        print(f"\nEl monto neto total facturado del destino {cod_dest} es {monto_total_B}")
    
    

                




menu()