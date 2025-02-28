class Navegable:
    def navegar(self):
        return "Navegando en el agua."

class Volador:
    def volar(self):
        return "Volando en el aire."

class Hidroavion(Navegable, Volador):
    def navegar(self):
        return "El hidroavión está navegando."

    def volar(self):
        return "El hidroavión está volando."

