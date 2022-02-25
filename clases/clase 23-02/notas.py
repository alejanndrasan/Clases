''' El viernes de semana 10: clase solo de practica!

Diagramas de clases:
Diagrama de estructura UML, muestra la estructura del sistema duh, es un cuadrito donde:
- Tiene el titulo arriba.
- Tiene dos subcuadritos:
    - Uno de atributos.
    - Otro de metodos.
El + y el - significan private y public (no se cual es cual).

Multiplicidad:
Es cuantas veces puedes instaciar de una clase: [m..n] #se escirbe asi, es un rango cerrado.

Asociacion:
Para asociar dos clases, se debe senalar que las asocia:
Ej: 
        1..*                0..*
Profesor-----Escribio----Libro #Se lee: uno o mas profesores escribieron cero o mas libros.

Agregacion:
Es cuando una clase principal tiene otra agregada, y la clase principal puede existir sin la clase agregada y viceversa.
Ej:
                  +sides
Triangulo<>------------Segemento
        1             3

Composicion:
Es cuando una clase principal tiene otra secundaria dentro de ella, pero su existencia depende de la principal.
Ej:
Folder <///>---------- Archivo

Generalizacion/Herencia:
Se senalizan con flechas que van desde los hijos a los padres.

Visibilidad:
+ --> Publico
- ---> Privado
# ---> Protected
~ ----> Default 

Para hacer UML ---> Lucid Chart

'''

print("Clase 23/02")