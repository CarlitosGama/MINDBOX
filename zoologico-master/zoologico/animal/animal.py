from datetime import datetime
from persona.utils.roles import Rol #Hacer un rol para animales, solo que me da TOC que se vea rojo jiji

class Animal:
    numero_control: str
    nombre: str
    apellido: str
    contrasenia: str
    curp: str
    rol: Rol
    fecha_nacimiento: datetime

    def __init__(self, numero_control: str, nombre: str, apellido: str, contrasenia: str, rol: Rol, curp:str, fecha_nacimiento:datetime):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = contrasenia
        self.rol = rol
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
        
#Tipo animal
#Fecha nacimiento
#Fecha llegada al zoológico
#Peso
#Enfermedades (Será un arreglo de cadenas en caso de que cuente con alguna/s)
#Frecuencia de alimentación
#Tipo de alimentación
#Cuenta con vacunas (valor booleano)
