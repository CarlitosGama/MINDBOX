#from random import randint
from typing import List
from datetime import datetime
from random import randint

from animal.animal import Animal
from empleado.empleado import Empleado       
from visitante.visitante import Visitante
from actividades.actividades import Actividad

class Zoologico:
         
    def __init__(self):
        self.lista_empleados: List[Empleado] = []
        self.lista_visitantes: List[Visitante] = []
        self.lista_animales: List[Animal] = []
        self.lista_animales = []  # Lista para almacenar los animales
        self.contador_animal = 1  
        self.contador_visita = 1  
        self.lista_actividades: List[Actividad] = [] 
    

    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        print(f"Visitante {visitante.nombre} registrado con éxito.")
        
    def generar_numero_control_visita(self):
        numero_control = f"VIS-{self.contador_visita:04d}"
        self.contador_visita += 1
        return numero_control

    def mostrar_visitante(self):
        if not self.lista_visitantes:
            print("No hay visitantes registrados.")
            return

        for visitante in self.lista_visitantes:
            print(
                f"Nombre: {visitante.nombre}, Visitas: {visitante.numero_visitas}, Numero de control: {visitante.numero_control}")

    def mostrar_visitante_frecuentes(self):
        if not self.lista_visitantes:
            print("No hay visitantes frecuentes registrados.")
            return

        for visitante in self.lista_visitantes:
            if visitante.numero_visitas >= 5:
                print(
                    f"Nombre: {visitante.nombre}, Visitas: {visitante.numero_visitas}, Numero de control: {visitante.numero_control}")
            else:
                print("No hay visitantes frecuentes")
                
    def buscar_visitante_por_control(self, control: str):
        for visitante in self.lista_visitantes:
            if visitante.numero_control == control:
                return visitante
        return None
    
    

    def registrar_actividad(self, empleado, animal_id, proceso, fecha, observaciones=None):
        nueva_actividad = Actividad(empleado, animal_id, proceso, fecha, observaciones)
        self.lista_actividades.append(nueva_actividad)
        print(f"Actividad registrada: {nueva_actividad}")


    def mostrar_actividades(self):
        if not self.lista_actividades:
            print("No hay actividades registradas.")
            return

        for actividad in self.lista_actividades:
            print(actividad)

    #def generar_id(self):
    #    nuevo_id = f"ZOO-{self.contador_id:04d}"  #ZOO-0001...0002
    #    self.contador_id += 1
    #    return nuevo_id
    
    def generar_numero_control_animal(self):
        numero_control = f"ANIM-{self.contador_animal:04d}"
        self.contador_animal += 1
        return numero_control

    def registrar_animal(self, animal: Animal):
        self.lista_animales.append(animal)
        print(f"Animal {animal.tipo_animal} con número de control {animal.numero_control} registrado con éxito.")

    def mostrar_animales(self):
        if not self.lista_animales:
            print("No hay animales registrados.")
            return
        
        for animal in self.lista_animales:
            animal.mostrar_informacion()

    def eliminar_animal(self, numero_control: str):
        """Elimina un animal usando su número de control"""
        for animal in self.lista_animales:
            if animal.numero_control == numero_control:
                self.lista_animales.remove(animal)
                print(f"Animal con número de control {numero_control} eliminado.")
                return
        print(f"No se encontró el animal con número de control {numero_control}.")
        
        
    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)
        print(f"Empleado {empleado.nombre} {empleado.apellido} RFC: {empleado.rfc}  registrado con éxito.")
    
    def mostrar_empleados(self, tipo_empleado=None):
        if not self.lista_empleados:
            print("No hay empleados registrados.")
            return
        
        for empleado in self.lista_empleados:
            if tipo_empleado is None or isinstance(empleado, tipo_empleado):
                print(f"Nombre: {empleado.nombre}, Tipo: {empleado.__class__.__name__}, RFC: {empleado.rfc}")

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
            

    def generar_numero_control(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_empleados) + 1
        aleatorio = randint(0, 10000)

        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        
        return numero_control