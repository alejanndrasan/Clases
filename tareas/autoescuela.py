#Autoescuela:

'''cedula del conductor, tipo de vehículo (Automático “A” o Sincrónico “S”), y el 
número de horas de clase que el cliente va a tomar. 
“A”: 2.500 
“S”: 3.500 
Cliente:
Imprimir para cada cliente su factura. 
15% de descuento si supera las 3 horas.
Para la autoescuela:
B1. La cantidad total de clientes
B2. La cantidad de clientes por tipo de vehículo
B3. La cantidad de clientes a quienes se les otorgo descuento
B4. El Promedio de Facturación por Tipo de Vehículo 
'''
def menu():
    cont_s = 0
    cont_a = 0
    while True: 
        while True:
            opciones = input('''\nBienvenido
            \nSeleccione la opcion que desee realizar:
            \n1. Registro y facturacion del cliente.
            \n2. Ver cantidad total de clientes.
            \n3. Ver clientes por tipo de vehiculo.
            \n4. Ver cantidad de clientes con descuento.
            \n5. Ver promedio de facturacion por tipo de vehiculo.
            \n6. Salir. ''')
            if opciones.isnumeric() and (int(opciones)==1 or int(opciones)==2 or int(opciones)==3 or int(opciones)==4 or int(opciones)==5 or int(opciones)==6):
                opciones = int(opciones)
                break
            else:
                print("Inserte una opcion valida")
        if opciones == 1:
            add_cliente(cont_s, cont_a)

#Registro y facturacion del cliente:
def add_cliente(cont_s, cont_a):
    clientes_list = []
    while True:
        cedula = input("CI: ")
        if cedula.isnumeric():
            break
        else:
            print('Inserte un numero de cedula valido.')
    while True:
        vehiculo = input('''Tipo de vehiculo:
        \n1. Sincronico.
        \n2. Automatico. 
        \n ==>   ''')
        if vehiculo.isnumeric() and (int(vehiculo)==1 or int(vehiculo)==2):
            vehiculo = int(vehiculo)
            break
        else:
            print('Inserte una opcion valida.')
    while True:
        horas_clase = input("Horas de clase que desea cursar: ")
        if horas_clase.isnumeric() and int(horas_clase)>0:
            horas_clase=int(horas_clase)
            break
        else:
            print('Inserte un numero de horas valido.')
    cliente = {
        "CI": cedula ,
        "Tipo de vehiculo": vehiculo,
        "Horas de clase": horas_clase ,
        }
    cliente.update()
    clientes_list.append(cliente)
    factura(cedula, vehiculo, horas_clase, cont_s, cont_a)

def factura(cedula, vehiculo, horas_clase, cont_s, cont_a):
    monto = 0
    if vehiculo == 1: #poner sinronico y eso
        tipo = "Sincronico"
        monto = horas_clase * 3500
        cont_s+=1
    if vehiculo ==2:
        tipo = "Automatico"
        monto = horas_clase * 2500
        cont_a += 1
    if horas_clase >= 3:
        monto = monto*0.15
    #Factura:
    print(f'''Factura:
    \nCI: {cedula}
    \nTipo de vehiculo: {tipo} 
    \nHoras de clase: {horas_clase}
    \nMonto:{monto}\n''')

menu()


    

    



