#!/usr/bin/env python3

class Vehiculos():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):

        print(" Marca:", self.marca, "\n Modelo: ", self.modelo, "\n En marcha: ", self.enmarcha, "\n Acelerando: ", self.acelera, "\n Frenando: ", self.frena)


class Furgoneta(Vehiculos):

    def carga(self, cargar):

        self.cargado = cargar

        if (self.cargado):

            return " La furgoneta está cargada"
        else:
            return " La furgoneta no está cargada"


class Moto(Vehiculos):
    
    hacecaballito = ""

    def caballito(self):

        self.hacecaballito = "Voy haciendo caballito"

    def estado(self):

        print(" Marca:", self.marca, "\n Modelo: ", self.modelo, "\n En marcha: ", self.enmarcha, "\n Acelerando: ", self.acelera, "\n Frenando: ", self.frena, "\n", self.hacecaballito)
    
class VElectricos():

    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):

        self.cargando == True

miMoto = Moto("Honda", "CBR")

miMoto.caballito()
miMoto.estado()
miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos, Vehiculos):
    pass

miBici = BicicletaElectrica()