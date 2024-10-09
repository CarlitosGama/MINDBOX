from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import rol

class Maestro(Usuario):

    rfc: str
    sueldo: float

    def __init__(self, numero_control: str, nombre: str, apellido: str, rfc: str, sueldo:  float,  contraseña:str):
        
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_M(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"numero de control: {self.numero_control}, nombre completo: {nombre_completo}, rfc: {self.rfc}, sueldo: {self.sueldo}"
        return info   