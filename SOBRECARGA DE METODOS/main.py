from vector import Vector
from transformador import Transformador

vector = Vector()
print(vector.calcular_norma(3, 4))
print(vector.calcular_norma(1, 2, 2))

transformador = Transformador()
datos = [1, 2, 3, 4, 5]
print(transformador.transformar(datos))
print(transformador.transformar(datos, 2))