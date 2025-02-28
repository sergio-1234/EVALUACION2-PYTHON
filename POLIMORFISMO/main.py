from empleado import Desarrollador, Disenador, Gerente

def mostrar_trabajo(empleados):
    for empleado in empleados:
        print(empleado.trabajar())

empleados = [Desarrollador(), Disenador(), Gerente()]
mostrar_trabajo(empleados)