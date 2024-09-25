class Materia:

    numero_control: str
    nombre: str
    descripcion: str
    semestre: int
    creditos: int


    def __init__(self, numero_control: str, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.numero_control = numero_control
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
