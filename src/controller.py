import threading
from model import Ciudad

class controller:
    def __init__(self, view):
        self.view = view
        self.ciudad = Ciudad()
        self.load_data()  # Cargar datos iniciales

    def load_data(self):
        # Agregar centros de operación
        self.ciudad.agregar_centro_operacion(1, 1000, 10, 5)
        self.ciudad.agregar_centro_operacion(2, 1500, 8, 6)

        # Agregar clientes
        self.ciudad.agregar_cliente(3, "Cliente A", 500, 30)
        self.ciudad.agregar_cliente(4, "Cliente B", 800, 45)

        # Agregar puentes
        self.ciudad.agregar_puente(5, 1000)

        # Agregar rutas
        self.ciudad.agregar_ruta(1, 3, 10)
        self.ciudad.agregar_ruta(2, 4, 20)
        self.ciudad.agregar_ruta(3, 4, 15)
        self.ciudad.agregar_ruta(4, 5, 25)

    def start_simulation(self):
        # Iniciar la simulación en un hilo separado
        threading.Thread(target=self.run_simulation).start()

    def run_simulation(self):
        # Lógica de simulación aquí
        pass

    def attack(self):
        # Lógica para manejar el evento de ataque
        pass
