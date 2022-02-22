#ejercicio de numeros semi perfectos:

'''todo número natural que cumple que es igual a la suma de algunos de sus divisores propios.
Por ejemplo, 18 es semiperfecto ya que sus divisores son 1, 2, 3, 6, 9 y se cumple que 3+6+9=18.'''

num_n = int(input("Ingresar numero: "))
divisores = []
semi_divisores = []


for x in range(1, num_n):
    if num_n%x == 0:
        divisores.append(x)

print(divisores)

aux = len(divisores)-1

for i in range(divisores[]):
    while aux > 0:
        if i + divisores[aux]:
            semi_divisores.append(i, divisores[aux])
        aux -= 1

print(semi_divisores)
