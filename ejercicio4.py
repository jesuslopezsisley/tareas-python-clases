# POLIFORMISMO CON CLASE ANIMAL

#Implementa polimorfismo:

"""Crea una clase abstracta Animal con un método abstracto hacer_sonido().
Crea clases concretas que hereden de Animal, por ejemplo, Perro y Gato,
e implementa el método hacer_sonido para cada uno de ellos de manera que
refleje el sonido específico que hace cada animal.
Demuestra cómo se pueden crear instancias de Perro y Gato y
cómo llamar al método hacer_sonido en objetos de ambas clases, 
mostrando así el polimorfismo."""

# tenemos que importar la clase abstracta y el decorador para el método abstracto.
from abc import ABC, abstractmethod 
# ABC es una clase que nos permite crear nuestras propias clases abstractas
# abstractmethod nos permite hacer nuestros metodos abstractos

class Animal(ABC):
    # creamos un metodo abstracto para Animal
    @abstractmethod
    def hacer_sonido():
        pass
    # no tiene codigo en su interior, es un método vacio
    # las clases hijas se ven obligadas a implementarlo

class perro(Animal):
    def hacer_sonido(self):
        print("guau!!")   # o return "guau"

class gato(Animal):
    def hacer_sonido(self):
        print("miau!!")   # o return "miau"

# crear instancias de perro y gato
perro=perro()  
gato=gato()    

animales=[perro,gato]

# Llamar al método hacer_sonido en objetos de ambas clases
for animal in animales:
    animal.hacer_sonido()