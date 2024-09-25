from datetime import datetime

class Maestro:
    numero_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float

    def __init__(self, numero_control: str, nombre: str, apellido: str, rfc: str, sueldo:  float):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_M(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"numero de control: {self.numero_control}, nombre completo: {nombre_completo}, rfc: {self.rfc}, sueldo: {self.sueldo}"
        return info   