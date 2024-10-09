from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    rfc: str
    sueldo: float

    def __init__(self, numeroControl: str, nombre: str, apellido: str, rfc: str, sueldo: float, contrasenia: str):
        super().__init__(
            numero_control=numeroControl,
            nombre=nombre,
            apellido=apellido,
            contrasenia=contrasenia,
            rol=Rol.MAESTRO
        )
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"\n - Número de control: {self.numero_control}, nombre completo: {nombre_completo}, RFC: {self.rfc}"
        return info
