from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from random import randint

class Grupo:
    id: str
    estudiantes: list[Estudiante] = []
    maestros: list[Maestro] = []
    materias: list[Materia] = []
    tipo: chr
    id_semestre = str


    def __init__(self, tipo: str,  id_semestre: str):
       self.id = self.generar_id()
       self.tipo = tipo
       self.id_semestre = id_semestre


    def generar_id(self, tipo: chr) -> str:
     return f"{tipo}-{randint(0, 100000)}-{randint(0, 100000)}"

    def mostrar_info_G(self):
        info = f"ID: {self.id}, tipo: {self.tipo}, ID de semestre: {self.id_semestre}"
        return info