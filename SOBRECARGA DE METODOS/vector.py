import math

class Vector:
    def calcular_norma(self, x, y, z=None):
        if z is None:
            return math.sqrt(x**2 + y**2)  # Norma en 2D
        else:
            return math.sqrt(x**2 + y**2 + z**2)  # Norma en 3D

