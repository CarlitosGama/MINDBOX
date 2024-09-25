from escuelas.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from datetime import datetime


escuela = Escuela()

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
    print("9.- Mostrar Grupos")
    print("10.- Eliminar Maestros")
    print("11.- Eliminar Estudiantes")
    print("12.- Eliminar Materias")
    print("13.- Salir")

    opcion = input("Ingresa una opcion para continuar: ")

    if opcion == "1":
      print("\n Seleccionaste la opcion para registrar un estudiante")
      
      numero_control_A = escuela.generar_num_control_A()

      nombre = input("Ingrese el nombre delestudiante:  ")
      apellido = input("Ingrese el apellido del estudiante: ")
      curp = input("Ingrese la curp del  estudiante: ")
      ano = int(input("Ingrese el ano de nacimiento del estudiante: "))
      mes = int(input("Ingrese el mes de nacimiento del estudiante: "))
      dia = int(input("Ingrese el dia de nacimiento del estudiante: "))
      print("\nNumero de control: ", numero_control_A)
      fecha_nacimiento = datetime(ano, mes, dia)
      estudiante = Estudiante(numero_control=numero_control_A, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
      escuela.registrar_estudiante(estudiante)

    if opcion == "2":
      print("\n Seleccionaste la opcion para registrar un estudiante")


      nombre = input("Ingrese el nombre del maestro:  ")
      apellido = input("Ingrese el apellido del maestro: ")
      rfc = input("Ingrese el rfc del  maestro: ")
      ano = int(input("Ingrese el ano de nacimiento del maestro: "))
      mes = int(input("Ingrese el mes de nacimiento del maestro: "))
      dia = int(input("Ingrese el dia de nacimiento del maestro: "))
      fecha_nacimiento = datetime(ano, mes, dia)

      numero_control_M = escuela.generar_num_control_M(ano=ano, nombre=nombre, rfc=rfc)

      sueldo = float(input("Ingrese el sueldo del maestro: "))
      maestro = Maestro(numero_control=numero_control_M, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
      escuela.registrar_maestro(maestro)
      print("\nNumero de control: ", numero_control_M) 

    if opcion == "3":
     print("\n Seleccionaste la opcion para registrar una materia")

     nombre = input("Ingrese el nombre de la materia: ")
     descripcion = input("Ingrese la drescripcion de la materia: ")
     semestre = input("Ingrese el semestre en el que se cursa la materia: ")
     creditos = input("Ingrese los creditos de la materia: ")

     numero_control_MT = escuela.generar_num_control_MT(nombre=nombre, semestre=semestre, creditos=creditos)

     print("\nNumero de control: ", numero_control_MT) 

    if opcion == "4":
     pass

    if opcion == "5":
     pass

    if opcion == "6":
     escuela.listar_Maestros()

    if opcion == "7":
     
     escuela.listar_estudiantes()

    if opcion == "8":
     escuela.listar_materias()

    if opcion == "9":
     pass

    if opcion == "10":
     print("\nSeleccionaste la opcion para eliminar un maestro")
     numero_control_F = input("Ingrese el numero de control del  maestro que desea eliminar: ")
     escuela.eliminar_maestro(numero_control=numero_control_F)

    if opcion == "11":
     print("\nSeleccionaste la opcion para eliminar un estudiante")
     numero_control_F = input("Ingrese el numero de control del  estudiante que desea eliminar: ")
     escuela.eliminar_estudiante(numero_control=numero_control_F)


    if opcion == "12":
     print("\nSeleccionaste la opcion para eliminar una materia")
     numero_control_F = input("Ingrese el numero de control de la  materia que desea eliminar: ")
     escuela.eliminar_materia(numero_control=numero_control_F)

    if opcion == "13":
     print("Hasta luego")
     break
    
