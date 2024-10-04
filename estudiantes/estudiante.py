from datetime import datetime
from ususario.usuario import Usuario
from ususario.utils import Rol

class Estudiante(Usuario):

    curp: str
    fecha_nacimiento: datetime


    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contraseña: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Rol.ESTUDIANTE)

        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info_E(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"numero de control: {self.numero_control}, nombre completo: {nombre_completo}, curp: {self.curp}"
        return info