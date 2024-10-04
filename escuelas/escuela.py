from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import  Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint


class Escuela:
    lista_estudiantes: list[Estudiante] = []
    lista_maestros: list[Maestro] = []
    lista_grupos: list[Grupo] = []
    lista_materias: list[Materia] = []
    lista_carreras: list[Carrera] = []
    lista_semestres: list[Semestre] = []
    

    def  registrar_estudiante(self,  estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
    
    def  registrar_maestro(self,  maestro: Maestro):
        self.lista_maestros.append(maestro)
    
    def  registrar_materia(self,  materia: Materia):
        self.lista_materias.append(materia)

    def  registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)

    def  registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre

        for semestre in self.lista_semestres:
           if id_semestre == semestre.id:
              semestre.registrar_grupo_en_semestre(grupo=grupo)
              break

        self.lista_grupos.append(grupo)

    def registrar_semestre(self, semestre: Semestre):
       id_carrera  = semestre.id

       for carrera in self.lista_carreras:
          if carrera.matricula == id_carrera:
             carrera.registrar_semestre(semestre=semestre)
             break

       self.lista_semestres.append(semestre)

    def generar_num_control_A(self):
      
      numero_control_A = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0,  1000)}"
      return numero_control_A
   
    def generar_num_control_MT(sefl, nombre, semestre, creditos):
      ultimos_2 = nombre[-2:]
      semestre_n = semestre
      creditos_n = creditos
      numero_control_MT = f"MT{ultimos_2}{semestre_n}{creditos_n}{randint(1,  1000)}"
      return numero_control_MT
    
    def generar_num_control_M(self, ano,  nombre, rfc):
      self.fecha_nacimiento = ano
      self.nombre = nombre
      self.rfc = rfc
      primeros_dos = nombre[:2]
      ultimos_dos = rfc[-2:]
      numero_control_M = f"M{self.fecha_nacimiento}{datetime.now().day}{randint(500,  5000)}{primeros_dos}{ultimos_dos}{len(self.lista_estudiantes) + 1}"
      return numero_control_M
    
    def  listar_estudiantes(self):
       print("****Estudiantes****")

       for estudiante in self.lista_estudiantes:
          print(estudiante.mostrar_info_E())
   
    def  listar_Semestres(self):
       print("****SEMESTRES****")

       for semestre in self.lista_semestres:
          print(semestre.mostrar_info_SM())
    
    def  listar_carreras(self):
       print("****CARRERAS****")

       for carrera in self.lista_carreras:
          print(carrera.mostrar_info_CA())
   
    def  listar_grupos(self):
       print("****GRUPOS****")

       for grupo in self.lista_grupos:
          print(grupo.mostrar_info_G())

    def eliminar_estudiante(self, numero_control: str):
       for estudiante in self.lista_estudiantes:
          if estudiante.numero_control ==  numero_control:
             self.lista_estudiantes.remove(estudiante)
             print("Estudiante eliminado")
             return
        
       print(f"No se encontró el estudiante con numero de control: {numero_control}") 


    def  listar_Maestros(self):
       print("****Maestros****")

       for maestro in self.lista_maestros:
          print(maestro.mostrar_info_M())

    def eliminar_maestro(self, numero_control: str):
       for maestro in self.lista_maestros:
          if maestro.numero_control ==  numero_control:
             self.lista_estudiantes.remove(maestro)
             print("Maestro eliminado")
             return
        
       print(f"No se encontró el maestro con numero de control: {numero_control}") 

    def  listar_materias(self):
       print("****Materias****")

       for materia in self.lista_materias:
          print(materia.mostrar_info_MT())

    def eliminar_materia(self, numero_control: str):
       for materia in self.lista_materias:
          if materia.numero_control ==  numero_control:
             self.lista_estudiantes.remove(materia)
             print("Materia eliminada")
             return
        
       print(f"No se encontró la materia con numero de control: {numero_control}") 
        
    def  listar_carreras(self):
       print("****Carreras****")

       for estudiante in self.lista_estudiantes:
          print(estudiante.mostrar_info_E())    