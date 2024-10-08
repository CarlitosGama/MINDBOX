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
    
    def  registrar_maestro(self,  maestro: Maestro):
        self.lista_maestros.append(maestro)


    def generar_num_control_A(self):
      
      numero_control_A = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0,  1000)}"
      return numero_control_A
    
    def generar_num_control_M(self, ano,  nombre, rfc):
      self.fecha_nacimiento = ano
      self.nombre = nombre
      self.rfc = rfc
      primeros_dos = nombre[:2]
      ultimos_dos = rfc[-2:]
      numero_control_M = f"M{self.fecha_nacimiento}{datetime.now().day}{randint(500,  5000)}{primeros_dos}{ultimos_dos}{len(self.lista_estudiantes) + 1}"
      return numero_control_M
    