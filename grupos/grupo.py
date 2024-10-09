from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from random import randint

class Grupo:
    id: str
    estudiantes: List[Estudiante] = []
    maestros: List[Maestro] = []
    materias: List[Materia] = []
    tipo: chr
    id_semestre: str

    def __init__(self, tipo: chr, id_semestre: str):
        self.id = self.generar_id()
        self.tipo = tipo
        self.id_semestre = id_semestre

    def generar_id(self, tipo: chr) -> str:
        return f"{tipo}-{randint(0, 100000)}-{randint(0, 100000)}"



"""
ID:
TIPO
ID: SEMESTRE
"""