from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import  Materia
from coordinador.coordinador import Coordinador
from usuario.usuario import Usuario
from datetime import datetime
from random import randint


class Escuela:
    lista_usuarios: List[Usuario] = []
    lista_estudiantes: list[Estudiante] = []
    lista_maestros: list[Maestro] = []
    lista_grupos: list[Grupo] = []
    liosta_materias: list[Materia] = []

    def __init__(self):
      coordinador = Coordinador(numeroControl="12345", nombre="Edson", apellido="Medina", rfc="MEDINA123", sueldo=100000, anios_antiguedad=10, contrasenia="123*")
      self.lista_usuarios.append(coordinador)

    def  registrar_estudiante(self,  estudiante: Estudiante):
        self.lista_usuarios.append(estudiante)
        self.lista_estudiantes.append(estudiante)
    
    def  registrar_maestro(self,  maestro: Maestro):
        self.lista_usuarios.append(maestro)
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
    

    def validar_inicio_sesion(self, numero_control:str, contraseña:str):
       for usuario in self.lista_usuarios:
          if usuario.numero_control ==  numero_control:
             if usuario.contraseña == contraseña:
                return  usuario
             
       return None