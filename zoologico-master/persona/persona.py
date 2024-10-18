from .utils.roles import Rol
from datetime import datetime


class Persona:
    numero_control: str
    nombre: str
    apellido: str
    contrasenia: str
    curp: str
    rol: Rol
    fecha_nacimiento: datetime

    def __init__(self, numero_control: str, nombre: str, apellido: str, contrasenia: str, rol: Rol, curp:str, fecha_nacimiento:datetime):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = contrasenia
        self.rol = rol
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento