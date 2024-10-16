from persona.persona import Persona
from datetime import datetime

class Visitante(Persona):
    numero_visitas = int
    fecha_registro = datetime

    def __init__(self, numero_control: str, nombre: str, apellido: str, contrasenia: str, fecha_nacimiento: datetime, numero_visitas = numero_visitas, fecha_registro = fecha_registro):
        super().__init__(
            numero_control=numero_control,
            nombre=nombre,
            apellido=apellido,
            contrasenia=contrasenia,
            rol=None,
            curp="",
            fecha_nacimiento=fecha_nacimiento
        )
        self.numero_visitas = numero_visitas
        self.fecha_registro = fecha_registro


#Nombre
#Apellidos
#Fecha de nacimiento
#CURP
#Número de visitas (inicialmente comienza en 0)
#Fecha de registro

#-----------------------------------------------------------


#{guia a carga de ella, $100 adulto, $50 niño
#+5 visitas, descuento del %20
#Guía a cargo
#Visitantes []
#Costo total de la visita (la suma de los boletos de los visitantes)
#Fecha de la visita
#Cantidad de niños (se puede calcular con las fechas de nacimiento)
#Cantidad de adultos (se puede calcular con las fechas de nacimiento)}
