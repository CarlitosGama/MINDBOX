from .utils.roles import Enum

class Usuario:
    numero_control:  str
    nombre: str
    apellido: str
    contraseña: str
    

    def __init__(self, numero_control: str, nombre: str, apellido: str, contraseña: str):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
