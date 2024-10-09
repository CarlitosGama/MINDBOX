from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    rfc: str
    sueldo: float
    anios_antiguedad: int

    def __init__(self, numeroControl: str, nombre: str, apellido: str, rfc: str, sueldo: float, contrasenia: str, anios_antiguedad: int):
        super().__init__(
            numero_control=numeroControl,
            nombre=nombre,
            apellido=apellido,
            contrasenia=contrasenia,
            rol=Rol.COORDINADOR
        )
        self.rfc = rfc
        self.sueldo = sueldo
        self.anios_antiguedad = anios_antiguedad
