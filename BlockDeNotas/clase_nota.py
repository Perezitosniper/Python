class nota:

    def __init__(self, id, estado, dato):
        self.id = id
        self.estado = estado
        self.dato = dato

    def __str__(self):
        return str(self.id) + "&" + str(self.estado) + "&" + str(self.dato)
