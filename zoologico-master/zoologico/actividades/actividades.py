from persona.utils.roles import Rol  
#from datetime import datetime

class Actividades:
    def __init__(self, numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, idioma):
        super().__init__(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento)
        self.idioma = idioma
        self.rol = Rol.GUIA 


#Empleado que encargada (debe ser un empleado con el rol de mantenimiento)
#ID del animal
#Proceso que se realizó (Mantenimiento, limpieza, alimentación, etc)
#Fecha del proceso
#Observaciones (opcional)