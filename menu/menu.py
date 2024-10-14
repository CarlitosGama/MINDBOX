from escuelas.escuela import Escuela
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
            print("3. Mostrar mi informacion")
            print("4. Salir")

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
            print("****MINDBOX****")
            print("1.- Registra Estudiante")
            print("2.- Registra Maestro")
            print("3.- Registra Materia")
            print("4.- Registra Grupo")
            print("5.- Registra Horario")
            print("6.- Mostrar Maestros")
            print("7.- Mostrar Estudiantes")
            print("8.- Mostrar Materias")
            print("9.- Mostrar Carreras")
            print("10.- Mostrar Grupos")
            print("11.- Mostrar Semestres")
            print("12.- Eliminar Maestros")
            print("13.- Eliminar Estudiantes")
            print("14.- Eliminar Materias")
            print("15.- Registrar carrera")
            print("16.- Registrar semestre")
            print("17.- Salir")

            opcion = input("Ingresa una opcion para continuar: ")

            if opcion == "1":
              print("\n Seleccionaste la opcion para registrar un estudiante")
              
              numero_control_A = self.escuela.generar_num_control_A()

              nombre = input("Ingrese el nombre delestudiante:  ")
              apellido = input("Ingrese el apellido del estudiante: ")
              curp = input("Ingrese la curp del  estudiante: ")
              ano = int(input("Ingrese el ano de nacimiento del estudiante: "))
              mes = int(input("Ingrese el mes de nacimiento del estudiante: "))
              dia = int(input("Ingrese el dia de nacimiento del estudiante: "))
              print("\nNumero de control: ", numero_control_A)
              fecha_nacimiento = datetime(ano, mes, dia)
              estudiante = Estudiante(numero_control=numero_control_A, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
              self.escuela.registrar_estudiante(estudiante)

            elif opcion == "2":
              print("\n Seleccionaste la opcion para registrar un estudiante")


              nombre = input("Ingrese el nombre del maestro:  ")
              apellido = input("Ingrese el apellido del maestro: ")
              rfc = input("Ingrese el rfc del  maestro: ")
              ano = int(input("Ingrese el ano de nacimiento del maestro: "))
              mes = int(input("Ingrese el mes de nacimiento del maestro: "))
              dia = int(input("Ingrese el dia de nacimiento del maestro: "))
              fecha_nacimiento = datetime(ano, mes, dia)

              numero_control_M = self.escuela.generar_num_control_M(ano=ano, nombre=nombre, rfc=rfc)

              sueldo = float(input("Ingrese el sueldo del maestro: "))
              maestro = Maestro(numero_control=numero_control_M, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
              self.escuela.registrar_maestro(maestro)
              print("\nNumero de control: ", numero_control_M) 

            elif opcion == "3":
             print("\n Seleccionaste la opcion para registrar una materia")

             nombre = input("Ingrese el nombre de la materia: ")
             descripcion = input("Ingrese la drescripcion de la materia: ")
             semestre = input("Ingrese el semestre en el que se cursa la materia: ")
             creditos = input("Ingrese los creditos de la materia: ")

             numero_control_MT = self.escuela.generar_num_control_MT(nombre=nombre, semestre=semestre, creditos=creditos)

             print("\nNumero de control: ", numero_control_MT) 

            elif opcion == "4":
             print("\nSeleccionaste la opcion para registrar un grupo")

             tipo = input("Ingresa el tipo de grupo (A/B)")
             id_semestre = input("Ingrese el ID del semestre al que pertenece el grupo")
     
             grupo = Grupo(tipo=tipo, id_semestre=id_semestre)

             self.escuela.registrar_grupo(grupo=grupo)


            elif opcion == "5":
             pass

            elif opcion == "6":
             self.escuela.listar_Maestros()

            elif opcion == "7":
     
                     self.escuela.listar_estudiantes()

            elif opcion == "8":
             self.escuela.listar_materias()

            elif opcion == "9": #carrera
             print("\nSeleccionaste la opcion para mostrar carreras")

            elif opcion == "10": #grupos
             pass

            elif opcion == "11": #semestres
             pass

            elif opcion == "12":
             print("\nSeleccionaste la opcion para eliminar un maestro")
             numero_control_F = input("Ingrese el numero de control del  maestro que desea eliminar: ")
             self.escuela.eliminar_maestro(numero_control=numero_control_F)

            elif opcion == "13":
             print("\nSeleccionaste la opcion para eliminar un estudiante")
             numero_control_F = input("Ingrese el numero de control del  estudiante que desea eliminar: ")
             self.escuela.eliminar_estudiante(numero_control=numero_control_F)


            elif opcion == "14":
             print("\nSeleccionaste la opcion para eliminar una materia")
             numero_control_F = input("Ingrese el numero de control de la  materia que desea eliminar: ")
             self.escuela.eliminar_materia(numero_control=numero_control_F)

    
            elif opcion == "15":
             print("\nSeleccionaste la opcion para registar una carrera")

             nombre = input("Ingrese el nombre de la carrera")

             carrera = Carrera(nombre=nombre)

            elif opcion ==  "16":
                print("\nSeleccionaste la opcion para regfistrar un semestre")

                numero = input("Ingrese el numero de semestre")
                id_carrera = input("Ingrese el ID de la carrera")
                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre)

     

            elif opcion == "17":
                print("Hasta luego")
                break