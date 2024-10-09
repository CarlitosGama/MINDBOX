from usuario.usuario import Usuario
from usuario.utils.roles import  rol

class Coordinador:
   rfc: str
   sueldo: float


   def __init__(self, numero_control:str, nombre:str, apellido:str, rfc:str, sueldo: float, contraseña:str, anios_antiguedad: int):
     super().__init__(
     numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=rol.COORDINADOR)
     self.rfc = rfc
     self.sueldo = sueldo
     self.anios_antiguedad = anios_antiguedad