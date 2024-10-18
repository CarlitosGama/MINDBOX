from persona.persona import Persona
from datetime import datetime

class Director(Persona):

    def __init__(self, numero_control: str, nombre: str, apellido: str, contrasenia: str, fecha_nacimiento: datetime):
        super().__init__(
            numero_control=numero_control,
            nombre=nombre,
            apellido=apellido,
            contrasenia=contrasenia,
            rol=None,
            curp="",
            fecha_nacimiento=fecha_nacimiento
        )
