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
    
    def registrar_estudiante_en_grupo(self, numero_control_estudiante: str, id_grupo: str):
       estudiante = self.buscar_estudiante_por_id(numero_control=numero_control_estudiante)

       if estudiante is None:
          print("No se encontro un estudiante con el numero de estudiante proporcionado ")
          return
       grupo = self.buscar_grupo_por_id(numero_control=id_grupo)
       #checar   

    
    def buscar_estudiante_por_id(self, numero_control:str):
       for estudiante in self.lista_estudiantes:
          if estudiante.numero_control ==  numero_control:
                return  estudiante
             
       return None
    
    def buscar_grupo_por_id(self, numero_control:str):
       for grupo in self.lista_grupos:
          if grupo.id ==  numero_control:
                return  grupo
             
       return None
    
    def buscar_maestro_por_id(self, numero_control:str):
       for maestro in self.lista_maestros:
          if maestro.numero_control ==  numero_control:
                return  maestro
             
       return None
    
    def ver_grupos_asignados_a_estudiantes(self, numero_control_estudiante):
       