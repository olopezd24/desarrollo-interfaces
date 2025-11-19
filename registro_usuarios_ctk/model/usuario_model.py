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
