from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import  Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: list[Estudiante] = []
    lista_maestros: list[Maestro] = []
    lista_grupos: list[Grupo] = []
    liosta_materias: list[Materia] = []

    def  registrar_estudiante(self,  estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)


    def generar_num_control(self):
      
      numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0,  1000)}"
      return numero_control