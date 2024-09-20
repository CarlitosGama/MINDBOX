from escuelas.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime

escuela = Escuela()

while True:
    print("****MINDBOX****")
    print("1.- Registra Estudiante")
    print("2.- Registra Maestro")
    print("3.- Registra Materia")
    print("4.- Registra Grupo")
    print("5.- Registra Horario")
    print("6.- Salir")

    opcion = input("Ingresa una opcion para continuar")

    if opcion == "1":
      print("\n Seleccionaste la opcion para registrar un estudiante")
      
      numero_control = escuela.generar_num_control()

      print(numero_control)

      nombre = input("Ingrese el nombre delestudiante:  ")
      apellido = input("Ingrese el apellido del estudiante: ")
      curp = input("Ingrese la curp del  estudiante: ")
      ano = int(input("Ingrese el ano de nacimiento del estudiante: "))
      mes = int(input("Ingrese el mes de nacimiento del estudiante: "))
      dia = int(input("Ingrese el dia de nacimiento del estudiante: "))
      fecha_nacimiento = datetime(ano, mes, dia)

    if opcion == "2":
     pass 

    if opcion == "3":
     pass

    if opcion == "4":
     pass

    if opcion == "5":
     pass

    if opcion == "6":
     print("Hasta luego")
     break
    
