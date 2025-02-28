from empleado_abstracto import EmpleadoTiempoCompleto, EmpleadoMedioTiempo

empleado1 = EmpleadoTiempoCompleto("Juan", 3000)
empleado2 = EmpleadoMedioTiempo("Maria", 20, 15)

print(empleado1.mostrar_info())
print(empleado2.mostrar_info())