from empleado.empleado import Empleado  
from persona.utils.roles import Rol  
#from datetime import datetime

class Mantenimiento(Empleado):
    def __init__(self, numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, area):
        super().__init__(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento)
        self.area = area
        self.rol = Rol.MANTENIMIENTO  