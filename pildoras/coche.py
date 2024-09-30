#!/usr/bin/env python3

class Coche():

    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):

        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo = self.chequeo_interno()

        if self.__enmarcha and chequeo:

            return "El auto está en marcha"
        
        elif(self.__enmarcha and chequeo == False):

            return "Algo va mal en el chequeo, no podemos arrancar"

        else:

            return "El auto está parado"


    def estado(self):
        
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


#  Zona de llamadas


miCoche = Coche()  # nuestro primer objeto, instanciamos una clase

print(miCoche.arrancar(True))

miCoche.estado()

print("------------------------- Creamos un nuevo coche--------------------------------")

miCoche2 = Coche()  # Mi coche 2 es una instancia de clase de la clase Coche
print(miCoche2.arrancar(False))

miCoche2.__ruedas = 2

miCoche2.estado()
