#Ejercicio 2: Clase Libro

class Libro:
    titulo = ""
    autor = ""
    anio_publicacion = None
    numero_paginas = None

    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print('Informacion del Libro:')
        print('Titulo:', self.titulo)
        print('Autor:', self.autor)
        print('Año de publicación:', self.anio_publicacion)
        print('Numero de paginas:', self.numero_paginas)

l1 = Libro("El Extraño Caso del Dr. Jekyll y Mr. Hyde","Robert Louis Stevenson", 1886, 125)

l1.mostrar_informacion()