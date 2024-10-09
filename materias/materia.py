from typing import List
from random import randint
from datetime import datetime

class Materia:
    nombre: str
    descripcion: str
    id_semestre: int
    creditos: int

    def __init__(self, nombre: str, descripcion: str, id_semestre: int, creditos: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_semestre = id_semestre
        self.creditos = creditos
        self.numero_control = self.generar_numero_control()
    
    def generar_numero_control(self):
        ultimos_dos_letras = self.nombre[-2:].upper()
        aleatorio = randint(1, 1000)
        return f"MT{ultimos_dos_letras}{self.id_semestre}{self.creditos}{aleatorio}"
    
    def mostrar_info_materia(self):
        info = f"\n - Nombre: {self.nombre}, id: {self.numero_control}"
        return info
