#from random import randint
from typing import List
from datetime import datetime
from random import randint

from actividades.actividades import Actividades
from animal.animal import Animal
from empleado.empleado import Empleado       
from visitante.visitante import Visitante


class Zoologico:


# OKEY, HOLA, NO SE HASTA DONDE LLEVE ESTE CODIGO PERO ESTAR SIGUIENTES OPCIONES SON LOS METODOS
# QUE AUN ME FALTAN POR HACER, YA CREE SUS FUNCIONES AQUI EN ZOOLOGICO PERO SOLO FUE UN COPY PASTE DE LOS OTROS
# COMO TAL AUN NO TIENEN ASIGNADAS BIEN SUS CLASES O COSAS QUE HACEN, ASI QUE TODAS LAS CLASES REFERENTES A ESTOS
# AUN NO ESTAN BIEN HECHAS Y ESE TIPO DE COSAS
#                self.registrar_visitante()
#            elif opcion == "9":
#                self.zoologico.mostrar_visitantes()
#            elif opcion == "10":
#                self.zoologico.mostrar_visitantes(frecuentes)
#            elif opcion == "11":
#                self.eliminar_visitante()
#            elif opcion == "12":
#                self.registrar_animal()
#            elif opcion == "13":
#                self.zoologico.mostrar_animales()
#            elif opcion == "14":
#                self.eliminar_animal()
#            elif opcion == "15":
#                self.registrar_nueva_actividad_empleados()
#            elif opcion == "16":
#                self.mostrar__actividades_realizadas_empleados()
#            elif opcion == "17":
#                print("Hasta luego.")
#                break
                
                   
    def __init__(self):
        self.lista_empleados: List[Empleado] = []
        self.lista_visitante: List[Visitante] = []
        self.lista_animales: List[Animal] = []
        self.lista_actividades_empleados: List[Actividades] = []

    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)
        print(f"Empleado {empleado.nombre} {empleado.apellido} RFC: {empleado.rfc}  registrado con éxito.")

#↓
#↓
#↓
#↓
#↓
    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitante.append(visitante)
        print(f"Empleado {visitante.nombre} {visitante.apellido} ID: {visitante.numero_control}  registrado con éxito.")

#    def registrar_animal(self, animal: Animal):
#        self.lista_empleados.append(empleado)
#        print(f"Empleado {empleado.nombre} {empleado.apellido} RFC: {empleado.rfc}  registrado con éxito.")
#    
#    def registrar_nueva_actividad_empleados(self, animal: Animal):
#        self.lista_empleados.append(empleado)
#        print(f"Empleado {empleado.nombre} {empleado.apellido} RFC: {empleado.rfc}  registrado con éxito.")
#↑
#↑
#↑
#↑
#↑
                
    def mostrar_empleados(self, tipo_empleado=None):
        if not self.lista_empleados:
            print("No hay empleados registrados.")
            return
        
        for empleado in self.lista_empleados:
            if tipo_empleado is None or isinstance(empleado, tipo_empleado):
                print(f"Nombre: {empleado.nombre}, Tipo: {empleado.__class__.__name__}, RFC: {empleado.rfc}")

#↓
#↓
#↓
#↓
#↓
#↓
#↓

    def mostrar_visitantes(self, visitante=None):
        if not self.lista_visitante:
            print("No hay empleados registrados.")
            return
        
        for visitante in self.lista_visitante:
            if visitante is None or isinstance(visitante):
                print(f"Nombre: {visitante.nombre} {visitante.apellido} , ID: {visitante.numero_control}")

#    def mostrar_visitantes_frecuentes_NOSESISEOCUPAOTROMETODO(self, frecuentes):
#        if not self.lista_empleados:
#            print("No hay empleados registrados.")
#            return
#        
#        for empleado in self.lista_empleados:
#            if tipo_empleado is None or isinstance(empleado, tipo_empleado):
#                print(f"Nombre: {empleado.nombre}, Tipo: {empleado.__class__.__name__}, RFC: {empleado.rfc}")
#
#    def mostrar_animales(self, tipo_empleado=None):
#        if not self.lista_empleados:
#            print("No hay empleados registrados.")
#            return
#        
#        for empleado in self.lista_empleados:
#            if tipo_empleado is None or isinstance(empleado, tipo_empleado):
#                print(f"Nombre: {empleado.nombre}, Tipo: {empleado.__class__.__name__}, RFC: {empleado.rfc}")
#    
#    def mostrar__actividades_realizadas_empleados(self, tipo_empleado=None):
#        if not self.lista_empleados:
#            print("No hay empleados registrados.")
#            return
#        
#        for empleado in self.lista_empleados:
#            if tipo_empleado is None or isinstance(empleado, tipo_empleado):
#                print(f"Nombre: {empleado.nombre}, Tipo: {empleado.__class__.__name__}, RFC: {empleado.rfc}")
#↑
#↑
#↑
#↑
#↑

    def buscar_empleado_por_rfc(self, rfc: str):
        for empleado in self.lista_empleados:
            if empleado.rfc == rfc:
                return empleado
        return None

    def eliminar_empleado(self, rfc: str):
        empleado = self.buscar_empleado_por_rfc(rfc)
        if empleado:
            self.lista_empleados.remove(empleado)
            print(f"Empleado {empleado.nombre} eliminado con éxito.")
        else:
            print(f"No se encontró un empleado con RFC {rfc}.")
            
#↓↓↓
#↓↓↓
#↓↓↓
    def eliminar_visitante(self, rfc: str):
        empleado = self.buscar_empleado_por_rfc(rfc)
        if empleado:
            self.lista_empleados.remove(empleado)
            print(f"Empleado {empleado.nombre} eliminado con éxito.")
        else:
            print(f"No se encontró un empleado con RFC {rfc}.")
    
    def eliminar_animal(self, rfc: str):
        empleado = self.buscar_empleado_por_rfc(rfc)
        if empleado:
            self.lista_empleados.remove(empleado)
            print(f"Empleado {empleado.nombre} eliminado con éxito.")
        else:
            print(f"No se encontró un empleado con RFC {rfc}.")
#↑↑↑
#↑↑↑
#↑↑↑


    def generar_numero_control(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_empleados) + 1
        aleatorio = randint(0, 10000)

        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        
        return numero_control