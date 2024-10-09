from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from semestre.semestre import Semestre
from carrera.carrera import Carrera
from grupos.grupo import Grupo
from datetime import datetime
from usuario.utils.roles import Rol

class Menu:
    escuela: Escuela = Escuela()

    def login(self):
        intentos = 0
        while intentos < 5:
            print("\n*** BIENVENIDO ***")
            print("Inicia Sesión para Continuar")

            numero_control = input("Ingresa tu número de control: ")
            contrasenia_usuario = input("Ingresa tu contraseña: ")

            usuario = self.escuela.validar_inicio_sesion(numero_control=numero_control, contrasenia=contrasenia_usuario)
            
            if usuario is None:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)
            else:
                if usuario.rol == Rol.ESTUDIANTE:
                    self.mostrar_menu_estudiante()
                    intentos = 0
                elif usuario.rol == Rol.MAESTRO:
                    self.mostrar_menu_maestro()
                    intentos = 0
                else:
                    self.mostrar_menu()
                    intentos = 0


        print("Máximos intentos de inicio de sesión alcanzados. Adiós")


    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("\nUsuario o contraseña incorrectos. Intenta de nuevo")
        return intentos_usuario + 1


    def mostrar_menu_estudiante(self):
        opcion = 0
        while opcion != 3:
            print("\n** MINDBOX **")
            print("1. Ver horario")
            print("2. Ver grupos")
            print("3. Salir")

            opcion = int(input("Ingresa una opción"))

            if opcion == 3:
                break

    def mostrar_menu_maestro(self):
        opcion = 0
        while opcion != 5:
            print("\n** MINDBOX **")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver materias")
            print("4. Ver alumnos")
            print("5. Salir")

            opcion = int(input("Ingresa una opción"))

            if opcion == 5:
                break


    def mostrar_menu(self):
        while True:
            print("\n** MINDBOX **")
            print("1. Registrar estudiante")
            print("2. Registrar maestro")
            print("3. Registrar materia")
            print("4. Registrar grupo")
            print("5. Registrar horario")
            print("6. Mostrar estudiantes")
            print("7. Mostrar maestros") # Tarea
            print("8. Mostrar materias") # Tarea
            print("9. Mostrar grupos")
            print("10. Eliminar estudiante")
            print("11. Eliminar maestro") # Tarea
            print("12. Eliminar materia") # Tarea
            print("13. Registrar carrera")
            print("14. Registrar carrera")
            print("15. Mostrar carreras")
            print("16. Salir")

            opcion = input("Ingresa una opción para continuar: ")

            if opcion == "1":
                print("\nSeleccionaste la opción para registrar un estudiante")

                numero_control = self.escuela.generar_numero_control()
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa la curp del estudiante: ")
                ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el día de nacimiento del estudiante: "))
                fecha_nacimiento = datetime(ano, mes, dia)

                contrasenia = input("Ingresa la contraseña del estudiante: ")

                estudiante = Estudiante(
                    numero_control=numero_control,
                    nombre=nombre, apellido=apellido,
                    curp=curp,
                    fecha_nacimiento=fecha_nacimiento,
                    contrasenia=contrasenia
                )
                self.escuela.registrar_estudiante(estudiante)

                print("\nEstudiante registrado correctamente")

            elif opcion == "2":
                print("\nSeleccionaste la opción para registrar un maestro")

                nombre_maestro = input("Ingresa el nombre del maestro: ")
                apellido_maestro = input("Ingresa el apellido del maestro: ")
                rfc_maestro = input("Ingresa el RFC del maestro: ")
                sueldo_maestro = float(input("Ingresa el sueldo del maestro: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))

                numero_control_maestro = self.escuela.generar_numero_control_maestro(nombre_maestro, rfc_maestro, ano_nacimiento)

                contrasenia = input("Ingresa la contraseña del maestro: ")

                nuevo_maestro = Maestro(
                    numeroControl=numero_control_maestro,
                    nombre=nombre_maestro,
                    apellido=apellido_maestro,
                    rfc=rfc_maestro,
                    sueldo=sueldo_maestro,
                    contrasenia=contrasenia
                )
                nuevo_maestro.numeroControl = numero_control_maestro

                self.escuela.registrar_maestro(nuevo_maestro)

                print(f"\nMaestro registrado con éxito. Número de control: {nuevo_maestro.numeroControl}")

            elif opcion == "3":
                print("\nSeleccionaste la opción para registrar una nueva materia")

                nombre_materia = input("Ingresa el nombre de la materia: ")
                descripcion_materia = input("Ingresa la descripción de la materia: ")
                semestre_materia = int(input("Ingresa el semestre de la materia: "))
                creditos_materia = int(input("Ingresa los créditos de la materia: "))

                nueva_materia = Materia(nombre=nombre_materia, descripcion=descripcion_materia, semestre=semestre_materia, creditos=creditos_materia)
                self.escuela.registrar_materia(nueva_materia)

                print(f"\nMateria registrada con éxito. Número de control: {nueva_materia.numero_control}")

            elif opcion == "4":
                print("\nSeleccionaste la opción para registrar un nuevo grupo")
                
                tipo = input("Ingresa el tipo de grupo (A/B)")
                id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo")

                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)

                self.escuela.registrar_grupo(grupo=grupo)

            elif opcion == "5":
                print("hla")
                for semestre in self.escuela.lista_carreras:

                    print(semestre.matricula)

            elif opcion == "6":
                self.escuela.listar_estudiantes()

            elif opcion == "7":
                self.escuela.listar_maestros()

            elif opcion == "8":
                self.escuela.listar_materias()

            elif opcion == "10":
                print("\nSeleccionaste la opción para eliminar un estudiantes")

                numero_control = input("Ingresa el número de control del estudiante")

                self.escuela.eliminar_estudiante(numero_control=numero_control)

            elif opcion == "13":
                print("\nSeleccionaste la opción para registrar una carrera")

                nombre = input("Ingresa el nombre de la carrera")

                carrera = Carrera(nombre=nombre)

                self.escuela.registrar_carrera(carrera=carrera)

            elif opcion == "14":
                print("\nSeleccionaste la opción para registrar un semestre")

                numero = input("Ingresa el numero del semestre")
                id_carrera = input("Ingresa el ID de la carrera")

                semestre = Semestre(numero=numero, id_carrera=id_carrera)

                self.escuela.registrar_semestre(semestre=semestre)

            elif opcion == "15":
                self.escuela.listar_carreras()

            elif opcion == "16":
                print("\nHasta luego")
                break
