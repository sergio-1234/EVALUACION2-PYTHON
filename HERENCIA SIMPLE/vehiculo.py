class Vehiculo:
    def arrancar(self):
        pass

    def parar(self):
        pass

class Carro(Vehiculo):
    def arrancar(self):
        return "El carro está arrancando."

    def parar(self):
        return "El carro se ha detenido."

