from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

    def mostrar_info(self):
        return f"Empleado a tiempo completo: {self.nombre}, Salario: {self.calcular_salario()}"

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

    def mostrar_info(self):
        return f"Empleado a medio tiempo: {self.nombre}, Salario: {self.calcular_salario()}"

