class Empleado:
    def trabajar(self):
        return ""

class Desarrollador(Empleado):
    def trabajar(self):
        return "Escribiendo código."

class Disenador(Empleado):
    def trabajar(self):
        return "Creando diseño gráfico."

class Gerente(Empleado):
    def trabajar(self):
        return "Gestionando el equipo."

