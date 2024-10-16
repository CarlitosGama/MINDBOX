from empleado.empleado import Empleado  
from persona.utils.roles import Rol  
#from datetime import datetime

class Guia(Empleado):
    def __init__(self, numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, idioma):
        super().__init__(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento)
        self.idioma = idioma
        self.rol = Rol.GUIA  



#   def mostrar_info_guia(self):
#       nombre_completo = f"{self.nombre} {self.apellido}"
#       info = f"\n - Número de control: {self.numero_control}, nombre completo: {nombre_completo}, curp: {self.curp}, fecha de nacimiento: {self.fecha_nacimiento}, rol: {self.rol.value}"
#       return info
