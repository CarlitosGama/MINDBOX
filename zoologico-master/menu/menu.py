from datetime import datetime

from zoologico.zoologico import Zoologico
from guia.guia import Guia
from veterinario.veterinario import Veterinario
from mantenimiento.mantenimiento import Mantenimiento
from administracion.administracion import Administracion
from animal.animal import Animal
from visitante.visitante import Visitante

class Menu:
    zoologico: Zoologico = Zoologico()

    def iniciar_menu(self):
        while True:
            print("\n------------ BIENVENIDO AL ZOOLÓGICO DE MORELIA ------------")
            print("1. Registrar empleado")
            print("2. Mostrar empleados")
            print("3. Mostrar guías")
            print("4. Mostrar veterinarios")
            print("5. Mostrar empleados de mantenimiento")
            print("6. Mostrar empleados de administración")
            print("7. Eliminar empleado")
            print("---------------------------------------------------------------")
            print("8. Registrar visitante")
            print("9. Mostrar visitantes")
            print("10. Mostrar visitantes frecuentes") 
            print("11. Eliminar visitante")
            print("---------------------------------------------------------------")
            print("12. Registrar animal")
            print("13. Mostrar animales")
            print("14. Eliminar animal")
            print("---------------------------------------------------------------")
            print("15. Registrar nueva actividad (empleados)")
            print("16. Mostrar activiadades realizadas")
            print("---------------------------------------------------------------")
            print("17. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.registrar_empleado()
            elif opcion == "2":
                self.zoologico.mostrar_empleados()
            elif opcion == "3":
                self.zoologico.mostrar_empleados(Guia)
            elif opcion == "4":
                self.zoologico.mostrar_empleados(Veterinario)
            elif opcion == "5":
                self.zoologico.mostrar_empleados(Mantenimiento)
            elif opcion == "6":
                self.zoologico.mostrar_empleados(Administracion)
            elif opcion == "7":
                self.eliminar_empleado()
            elif opcion == "8":
                self.registrar_visitante()
            elif opcion == "9":
                self.zoologico.mostrar_visitante()
            elif opcion == "10":
                self.zoologico.mostrar_visitante_frecuentes()
            elif opcion == "11":
                self.eliminar_visitante()
            elif opcion == "12":
                self.registrar_animal()
            elif opcion == "13":
                self.zoologico.mostrar_animales()
            elif opcion == "14":
                self.eliminar_animal()
            elif opcion == "15":
                self.registrar_nueva_actividad_empleados()
            elif opcion == "16":
                self.mostrar_actividades_realizadas_empleados()
            elif opcion == "17":
                print("Hasta luego.")
                break
            else:
                print("Opción inválida, intenta de nuevo.")

    def registrar_empleado(self):
        print("\nSeleccionaste registrar un empleado.")
        tipo = input("Ingresa el tipo de empleado (guia/veterinario/mantenimiento/administracion): ").lower()

        # Información común a todos los empleados
        numero_control = self.zoologico.generar_numero_control
        nombre = input("Nombre del empleado: ")
        apellido = input("Apellido del empleado: ")
        rfc = input("RFC del empleado: ")
        sueldo = float(input("Sueldo del empleado: "))
        contrasenia = input("Contraseña: ")
        anios_antiguedad = int(input("Años de antigüedad: "))
        horario = input("Horario del empleado: ")
        fecha_nacimiento = self.ingresar_fecha_nacimiento()

        if tipo == "guia":
            idioma = input("Idioma del guía: ")
            nuevo_empleado = Guia(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, idioma)
        elif tipo == "veterinario":
            especialidad = input("Especialidad del veterinario: ")
            nuevo_empleado = Veterinario(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, especialidad)
        elif tipo == "mantenimiento":
            area = input("Área de mantenimiento: ")
            nuevo_empleado = Mantenimiento(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, area)
        elif tipo == "administracion":
            puesto = input("Puesto en la administración: ")
            nuevo_empleado = Administracion(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, puesto)
        else:
            print("Tipo de empleado no válido. Intenta de nuevo.")
            return
            
        self.zoologico.registrar_empleado(nuevo_empleado)
    
    
   # def __init__(self, zoologico):
   #     self.zoologico = zoologico

    def ingresar_fecha_llegada(self):
        
        fecha_str = input("Fecha de llegada (DD/MM/AAAA): ") #Método auxiliar para ingresar la fecha de llegada del animal
        return datetime.strptime(fecha_str, "%d/%m/%Y")
    
    def registrar_animal(self):
        print("\nSeleccionaste registrar un animal.")
    
        tipo_animal = input("Tipo de animal: ").capitalize()
        fecha_llegada = self.ingresar_fecha_llegada()  
        peso = float(input("Peso del animal (kg): "))

        enfermedades = input("Enfermedades (si tiene más de una, sepáralas por comas): ").split(',') 
        enfermedades = [enfermedad.strip() for enfermedad in enfermedades if enfermedad]  # Limpia espacios

        frecuencia_alimentacion = input("Frecuencia de alimentación: ")
        tipo_alimentacion = input("Tipo de alimentación: ")
        vacunas = input("¿Tiene vacunas? (sí/no): ").lower() == "sí"

        numero_control = self.zoologico.generar_numero_control_animal()

        nuevo_animal = Animal(
            numero_control=numero_control,
            tipo_animal=tipo_animal,
            fecha_llegada=fecha_llegada,
            peso=peso,
            enfermedades=enfermedades,
            frecuencia_alimentacion=frecuencia_alimentacion,
            tipo_alimentacion=tipo_alimentacion,
            vacunas=vacunas
        )
        
        self.zoologico.registrar_animal(nuevo_animal)

    def mostrar_animales(self):
        print("\nAnimales registrados:")
        self.zoologico.mostrar_animales()

    def eliminar_animal(self):
        print("\nSeleccionaste eliminar un animal.")
        numero_control = input("Ingresa el número de control del animal a eliminar: ")
        self.zoologico.eliminar_animal(numero_control)

    def eliminar_visitante(self):
        print("\nSeleccionaste eliminar un visitante.")
        numero_control = input("Ingresa el número de control del visitante a eliminar: ")
        self.zoologico.eliminar_visitante(numero_control)

    
    def eliminar_empleado(self):
        print("\nSeleccionaste eliminar un empleado.")
        rfc = input("Ingresa el RFC del empleado a eliminar: ")
        self.zoologico.eliminar_empleado(rfc)

    def ingresar_fecha_nacimiento(self):
        ano = int(input("Año de nacimiento: "))
        mes = int(input("Mes de nacimiento: "))
        dia = int(input("Día de nacimiento: "))
        return datetime(ano, mes, dia)
    
    
    def registrar_nueva_actividad_empleados(self):
        
        print("\nSeleccionaste registrar nueva actividad.")

        empleado = input("Ingresa el nombre del empleado: ")
        animal_id = input("Ingresa el ID del animal: ")
        proceso = input("Proceso realizado (Mantenimiento, limpieza, alimentación, etc.): ")
        fecha = input("Fecha del proceso (DD/MM/AAAA): ")
        observaciones = input("Observaciones (opcional): ")

    # Aquí se registra la actividad en el zoológico
        self.zoologico.registrar_actividad(empleado, animal_id, proceso, fecha, observaciones)

    def mostrar_actividades_realizadas_empleados(self):
        print("\nSeleccionaste mostrar actividades realizadas.")
        self.zoologico.mostrar_actividades()
   
#:)
    def ingresar_fecha_registro(self):
        ano = int(input("Año de registro: "))
        mes = int(input("Mes de registro: "))
        dia = int(input("Día de registro: "))
        return datetime(ano, mes, dia)

    def ingresar_fecha_visita(self):
        ano = int(input("Año de visita: "))
        mes = int(input("Mes de visita: "))
        dia = int(input("Día de visita: "))
        return datetime(ano, mes, dia)

    def elegir_visitante(self):
        print("\nSeleccionaste visitante previo.")
        numerodecontrol = input("Ingresa el Numero de control del visitante: ")
        visita = self.zoologico.buscar_visitante_por_control(numerodecontrol)
        visita.numero_visitas = visita.numero_visitas + 1
        return visita

    def registrar_visitante(self):
        fecha_visita = self.ingresar_fecha_visita()
        print(fecha_visita)
        print("\nSeleccionaste registrar un visitante, por favor elige el rfc tu guia: ")
        self.zoologico.mostrar_empleados(Guia)
        if not self.zoologico.lista_empleados:
            return

        guia = input("\n")
        empleado = self.zoologico.buscar_empleado_por_rfc(guia)

        if empleado:
            print("Tu guia es: " + empleado.nombre)
        else:
            print("No se encontró un guia con ese RFC.")
            return

        tanda = "1"
        costo = 0
        while tanda == "1":


            c = input("1. Si es un visitante nuevo o 2. Si es un visitante previo: ")

            if c == "1":

                numero_control = self.zoologico.generar_numero_control_visita()
                nombre = input("Nombre del visitante: ")
                apellido = input("Apellido del visitante: ")
                numero_visitas = 1
                contrasenia = input("Contraseña: ")
                fecha_nacimiento = self.ingresar_fecha_nacimiento()
                fecha_registro = self.ingresar_fecha_registro()
                edad = "Adulto" if fecha_nacimiento.year <= 2006 else "Niño"

                nuevo_visitante = Visitante(numero_control, nombre, apellido, contrasenia, fecha_nacimiento,
                                            numero_visitas,
                                            fecha_registro, edad)
                self.zoologico.registrar_visitante(nuevo_visitante)
                costo = (costo + 100) if nuevo_visitante.edad == "Adulto" else (costo + 50)
                if (nuevo_visitante.numero_visitas % 5) == 0:
                    costo = (costo - 20) if nuevo_visitante.edad == "Adulto" else (costo - 10)

            elif c == "2":
                if not self.zoologico.lista_visitantes:
                    return
                self.zoologico.mostrar_visitante()
                visita = self.elegir_visitante()
                print(
                    f"Nombre: {visita.nombre}, Visitas: {visita.numero_visitas}, Numero de control: {visita.numero_control}, Edad: {visita.edad}")
                costo = (costo + 100) if visita.edad == "Adulto" else (costo + 50)
                if (visita.numero_visitas % 5) == 0:
                    costo = (costo - 20) if visita.edad == "Adulto" else (costo - 10)

            tanda = input("1. Para seguir agregando miembros a la visita y 2. para terminar: ")

        print("Costo total del grupo: ", costo, " Guia que los acompañara: ", empleado.nombre)
        