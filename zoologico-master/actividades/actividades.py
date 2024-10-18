class Actividad:
    def __init__(self, empleado, animal_id, proceso, fecha, observaciones=None):
        self.empleado = empleado
        self.animal_id = animal_id
        self.proceso = proceso
        self.fecha = fecha
        self.observaciones = observaciones

    def __str__(self):
        observaciones_str = f" | Observaciones: {self.observaciones}" if self.observaciones else ""
        return f"Empleado: {self.empleado} | ID Animal: {self.animal_id} | Proceso: {self.proceso} | Fecha: {self.fecha}{observaciones_str}"