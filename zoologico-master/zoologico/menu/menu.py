from datetime import datetime

from zoologico.zoologico import Zoologico
from guia.guia import Guia
from veterinario.veterinario import Veterinario
from mantenimiento.mantenimiento import Mantenimiento
from administracion.administracion import Administracion

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
                self.zoologico.mostrar_visitantes()
            elif opcion == "10":
                self.zoologico.mostrar_visitantes(frecuentes)
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
                self.mostrar__actividades_realizadas_empleados()
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

    def eliminar_empleado(self):
        print("\nSeleccionaste eliminar un empleado.")
        rfc = input("Ingresa el RFC del empleado a eliminar: ")
        self.zoologico.eliminar_empleado(rfc)

    def ingresar_fecha_nacimiento(self):
        ano = int(input("Año de nacimiento: "))
        mes = int(input("Mes de nacimiento: "))
        dia = int(input("Día de nacimiento: "))
        return datetime(ano, mes, dia)




















#from zoologico.zoologico import Zoologico
#from empleado.empleado import Empleado
#from visitante.visitante import Visitante
#from animal.animal import Animal
#from guia.guia import Guia
#from veterinario.veterinario import Veterinario
#from mantenimiento.mantenimiento import Mantenimiento
#from administracion.administracion import Administracion
#from datetime import datetime
#from usuario.utils.roles import Rol
#
#class Menu:
#    zoologico: Zoologico = Zoologico()
#
#    def login(self):
#        intentos = 0
#        while intentos < 5:
#            print("\n------------ BIENVENIDO AL ZOOLOGICO DE MORELIA ----------")
#            print("Inicia Sesión para Continuar")
#
#            numero_empleado = input("Ingresa tu número de empleado: ")
#            contrasenia_usuario = input("Ingresa tu contraseña: ")
#
#            usuario = self.zoologico.validar_inicio_sesion(numero_empleado=numero_empleado, contrasenia=contrasenia_usuario)
#            
#            if usuario is None:
#                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)
#            else:
#                if usuario.rol == Rol.GUIA:
#                    self.mostrar_menu_guia()
#                    intentos = 0
#                elif usuario.rol == Rol.VETERINARIO:
#                    self.mostrar_menu_veterinario()
#                    intentos = 0
#                elif usuario.rol == Rol.MANTENIMIENTO:
#                    self.mostrar_menu_mantenimiento()
#                    intentos = 0
#                elif usuario.rol == Rol.ADMINISTRACION:
#                    self.mostrar_menu_administracion()
#                    intentos = 0
#                else:
#                    print("Rol no identificado. Contacte al administrador.")
#                    intentos += 1
#
#        print("Máximos intentos de inicio de sesión alcanzados. Adiós")
#
#    def mostrar_intento_sesion_fallido(self, intentos_usuario):
#        print("\nUsuario o contraseña incorrectos. Intenta de nuevo")
#        return intentos_usuario + 1
#
#    def mostrar_menu_guia(self):
#        opcion = 0
#        while opcion != 3:
#            print("\n** MENÚ DEL GUÍA **")
#            print("1. Ver lista de visitas guiadas")
#            print("2. Ver lista de visitantes")
#            print("3. Salir")
#
#            opcion = int(input("Ingresa una opción: "))
#
#            if opcion == 3:
#                break
#
#    def mostrar_menu_veterinario(self):
#        opcion = 0
#        while opcion != 4:
#            print("\n** MENÚ DEL VETERINARIO **")
#            print("1. Ver lista de animales")
#            print("2. Registrar nuevo tratamiento")
#            print("3. Ver historial de tratamientos")
#            print("4. Agregar enfermedad diagnosticada a un Animal")
#
#            print("5. Salir")
#
#            opcion = int(input("Ingresa una opción: "))
#
#            if opcion == 5:
#                break
#
#    def mostrar_menu_mantenimiento(self):
#        opcion = 0
#        while opcion != 3:
#            print("\n** MENÚ DE MANTENIMIENTO **")
#            print("1. Ver lista de tareas de mantenimiento")
#            print("2. Registrar nueva tarea")
#            print("3. Salir")
#
#            opcion = int(input("Ingresa una opción: "))
#
#            if opcion == 3:
#                break
#
#    def mostrar_menu_administracion(self):
#        while True:
#            print("\n** MENÚ DE ADMINISTRACIÓN **")
#            print("1. Registrar empleado")
#            print("2. Registrar visitante")
#            print("3. Registrar animal")
#            print("4. Mostrar empleados")
#            print("5. Mostrar visitantes")
#            print("6. Mostrar animales")
#            print("7. Eliminar empleado")
#            print("8. Eliminar visitante")
#            print("9. Eliminar animal")
#            print("10. Salir")
#
#            opcion = input("Ingresa una opción para continuar: ")
#
#            if opcion == "1":
#                print("\nSeleccionaste la opción para registrar un empleado")
#
#                numero_empleado = self.zoologico.generar_numero_empleado()
#                nombre = input("Ingresa el nombre del empleado: ")
#                apellido = input("Ingresa el apellido del empleado: ")
#                rol = input("Ingresa el rol del empleado (Guía, Veterinario, Mantenimiento, Administración): ")
#                contrasenia = input("Ingresa la contraseña del empleado: ")
#
#                empleado = Empleado(
#                    numero_empleado=numero_empleado,
#                    nombre=nombre, 
#                    apellido=apellido,
#                    rol=rol,
#                    contrasenia=contrasenia
#                )
#                self.zoologico.registrar_empleado(empleado)
#
#                print("\nEmpleado registrado correctamente")
#
#            elif opcion == "2":
#                print("\nSeleccionaste la opción para registrar un visitante")
#
#                nombre_visitante = input("Ingresa el nombre del visitante: ")
#                apellido_visitante = input("Ingresa el apellido del visitante: ")
#                edad_visitante = int(input("Ingresa la edad del visitante: "))
#                tipo_visita = input("Ingresa el tipo de visita (General/Guiada): ")
#
#                visitante = Visitante(nombre=nombre_visitante, apellido=apellido_visitante, edad=edad_visitante, tipo_visita=tipo_visita)
#                self.zoologico.registrar_visitante(visitante)
#
#                print("\nVisitante registrado correctamente")
#
#            elif opcion == "3":
#                print("\nSeleccionaste la opción para registrar un nuevo animal")
#
#                nombre_animal = input("Ingresa el nombre del animal: ")
#                especie_animal = input("Ingresa la especie del animal: ")
#                edad_animal = int(input("Ingresa la edad del animal: "))
#                habitat_animal = input("Ingresa el hábitat del animal: ")
#
#                animal = Animal(nombre=nombre_animal, especie=especie_animal, edad=edad_animal, habitat=habitat_animal)
#                self.zoologico.registrar_animal(animal)
#
#                print("\nAnimal registrado con éxito")
#
#            elif opcion == "4":
#                self.zoologico.mostrar_empleados()
#
#            elif opcion == "5":
#                self.zoologico.mostrar_visitantes()
#
#            elif opcion == "6":
#                self.zoologico.mostrar_animales()
#
#            elif opcion == "7":
#                print("\nSeleccionaste la opción para eliminar un empleado")
#
#                numero_empleado = input("Ingresa el número de empleado: ")
#                self.zoologico.eliminar_empleado(numero_empleado=numero_empleado)
#
#            elif opcion == "8":
#                print("\nSeleccionaste la opción para eliminar un visitante")
#
#                id_visitante = input("Ingresa el ID del visitante: ")
#                self.zoologico.eliminar_visitante(id_visitante=id_visitante)
#
#            elif opcion == "9":
#                print("\nSeleccionaste la opción para eliminar un animal")
#
#                id_animal = input("Ingresa el ID del animal: ")
#                self.zoologico.eliminar_animal(id_animal=id_animal)
#
#            elif opcion == "10":
#                print("\nHasta luego")
#                break
#