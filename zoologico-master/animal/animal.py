from datetime import datetime
from typing import List


class Animal:
    def __init__(self, numero_control: str, tipo_animal: str, fecha_llegada: datetime, peso: float, enfermedades: List[str], frecuencia_alimentacion: str, tipo_alimentacion: str, vacunas: bool):
        self.numero_control = numero_control
        self.tipo_animal = tipo_animal
        self.fecha_llegada = fecha_llegada
        self.peso = peso
        self.enfermedades = enfermedades
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.tipo_alimentacion = tipo_alimentacion
        self.vacunas = vacunas

    def mostrar_informacion(self):
        print(f"Animal: {self.tipo_animal} | No. Control: {self.numero_control} | Peso: {self.peso} kg | Vacunas: {'Sí' if self.vacunas else 'No'}")
        print(f"Fecha de llegada: {self.fecha_llegada}")
        print(f"Enfermedades: {', '.join(self.enfermedades) if self.enfermedades else 'Ninguna'}")
        print(f"Frecuencia de alimentación: {self.frecuencia_alimentacion} | Tipo de alimentación: {self.tipo_alimentacion}")
        print("--------------------------------------------------")
    
      
               
#Tipo animal
#Fecha nacimiento
#Fecha llegada al zoológico
#Peso
#Enfermedades (Será un arreglo de cadenas en caso de que cuente con alguna/s)
#Frecuencia de alimentación
#Tipo de alimentación
#Cuenta con vacunas (valor booleano)