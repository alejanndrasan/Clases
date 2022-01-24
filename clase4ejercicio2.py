#tablas de multiplicacion

print("Welcome to the multiplication table!")

def main():
    num = int(input("Enter a number> \n ==> "))
    cont = 1
    resultados = []
    while cont <= 12:
        resultadoN = num * cont
        resultados.append(resultadoN)
        cont += 1

    print(resultados)

main()

