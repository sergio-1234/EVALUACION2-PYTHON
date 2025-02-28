class Transformador:
    def transformar(self, datos, factor=None):
        if factor is None:
            return sum(datos)  
        else:
            return [x * factor for x in datos]  