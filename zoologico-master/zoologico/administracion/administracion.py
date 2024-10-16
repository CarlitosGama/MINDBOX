from empleado.empleado import Empleado  
from persona.utils.roles import Rol  
#from datetime import datetime


class Administracion(Empleado):
    def __init__(self, numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, puesto):
        super().__init__(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento)
        self.puesto = puesto

        self.rol = Rol.ADMINISTRACION  