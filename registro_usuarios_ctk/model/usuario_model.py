import csv


class Usuario:
    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar


class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana Pérez", 25, "F", "avatar1.png"))
        self._usuarios.append(Usuario("Carlos Gómez", 30, "M", "avatar2.png"))
        self._usuarios.append(Usuario("Niky", 22, "F", "avatar3.png"))

    def listar(self):
        return self._usuarios

    def añadir_usuario(self, usuario):
        self._usuarios.append(usuario)

    def guardar_csv(self, ruta):
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "edad", "genero", "avatar"])
            for u in self._usuarios:
                writer.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                lector = csv.reader(f)
                next(lector, None)
                self._usuarios.clear()

                for fila in lector:
                    try:
                        nombre, edad, genero, avatar = fila
                        edad_int = int(edad)
                        self._usuarios.append(Usuario(nombre, edad_int, genero, avatar))
                    except Exception:
                        continue

        except FileNotFoundError:
            return
