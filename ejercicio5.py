# USO DE SUPER() Herencia multiple

"""Crea una clase base Forma con un método dibujar() que simplemente imprime "Dibujando forma".
Crea otra clase base Color con un método pintar() que imprime "Pintando con [color]" donde [color] 
es un atributo de la clase. Crea una clase CuadradoColorido que herede de ambas clases, Forma y Color,
 y utiliza super() para llamar a los métodos de las clases padres de manera 
 adecuada para demostrar cómo se puede trabajar con herencia múltiple."""
# creamos la clase base FORMA
class Forma:
    def dibujar(self):
        print("Dibujando forma")
# creamos la clase base COLOR
class Color:
    def __init__(self, color):
        self.color = color
# hacemos el metodo
    def pintar(self):
        print(f"Pintando con color: {self.color}")

class CuadradoColorido(Forma, Color):
    def __init__(self, color):
        # Llamamos al constructor de cada clase base en orden
        Forma.__init__(self)
        Color.__init__(self, color)
        

    def dibujar(self):
        super().dibujar()
    
    def pintar(self):
        super().pintar()

# Crear un objeto de la clase CuadradoColorido
cuadrado = CuadradoColorido( "blanco")

# Llamar a los métodos dibujar() y pintar() de la clase CuadradoColorido
cuadrado.dibujar()  # obtendremos como resultado: Dibujando forma
cuadrado.pintar()   # obtendremos como resultado: Pintando con rojo



