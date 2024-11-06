try:
    numero_1 = 10
    numero_2 = 0

    division = numero_1/numero_2

    print(division)

except ZeroDivisionError as e:
    print(f"Estas tratando de dividir entre 0. {e}")