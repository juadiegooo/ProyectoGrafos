import sys
import threading
from model import Ciudad, Vehiculo, Escolta
import time
import networkx as nx
sys.path.append('./src')

class Controller:
    def __init__(self, view):
        self.view = view
        self.ciudad = Ciudad()
        self.vehiculos = []
        self.escoltas = []
        self.pedidos = []  # Lista de pedidos pendientes
        self.load_data()  # Cargar datos iniciales

    #creamos la ciudad y asignamos vehiculos de transporte
    def load_data(self):
        self.ciudad.agregar_centro_operacion(1, 1000, 10, 5)
        self.ciudad.agregar_cliente(2, "Cliente A", 500, 30)
        self.ciudad.agregar_cliente(3, "Cliente B", 800, 45)
        self.ciudad.agregar_cliente(4, "Cliente C", 800, 45)
        self.ciudad.agregar_cliente(5, "Cliente D", 800, 45)
        self.ciudad.agregar_cliente(6, "Cliente E", 800, 45)
        self.ciudad.agregar_puente(7, 1000)
        self.ciudad.agregar_puente(8, 1000)
        self.ciudad.agregar_puente(9, 1000)
        self.ciudad.agregar_puente(10, 1000)
        self.ciudad.agregar_puente(11, 1000)
        self.ciudad.agregar_puente(12, 1000)
        self.ciudad.agregar_puente(13, 1000)
        self.ciudad.agregar_puente(14, 1000)
        self.ciudad.agregar_puente(15, 1000)
        self.ciudad.agregar_puente(16, 1000)
        self.ciudad.agregar_puente(17, 1000)
        self.ciudad.agregar_ruta(1, 7, 10)
        self.ciudad.agregar_ruta(1, 17,10)
        self.ciudad.agregar_ruta(2, 9,10)
        self.ciudad.agregar_ruta(9, 8,10)
        self.ciudad.agregar_ruta(8, 7,10)
        self.ciudad.agregar_ruta(17, 14,10)
        self.ciudad.agregar_ruta(14, 5,10)
        self.ciudad.agregar_ruta(11, 10,10)
        self.ciudad.agregar_ruta(12, 17,10)
        self.ciudad.agregar_ruta(12, 8,10)
        self.ciudad.agregar_ruta(3, 11,10)
        self.ciudad.agregar_ruta(14, 13,10)
        self.ciudad.agregar_ruta(14, 11,10)
        self.ciudad.agregar_ruta(16, 4,10)
        self.ciudad.agregar_ruta(16, 11,10)
        self.ciudad.agregar_ruta(5, 15,10)
        self.ciudad.agregar_ruta(15, 14, 10)
        self.ciudad.agregar_ruta(6, 14, 10)
        
         # Agregar vehículos
        self.vehiculos.append(Vehiculo('pequeño', 500, 5, 10, 1))
        self.vehiculos.append(Vehiculo('grande', 1000, 20, 15, 2))

        # Agregar escoltas
        self.escoltas.append(Escolta(5, 5))
        self.escoltas.append(Escolta(5, 5))
        
        # Agregar pedidos
        self.pedidos.append({'origen': 1, 'destino': 3, 'dinero': 300})
        self.pedidos.append({'origen': 1, 'destino': 4, 'dinero': 700})


    def asignar_vehiculos_y_escoltas(self):
        if self.pedidos:
            pedido = self.pedidos.pop(0)
            for vehiculo in self.vehiculos:
                if vehiculo.capacidad >= pedido['dinero']:
                    escoltas_necesarias = vehiculo.escoltas_necesarias
                    escoltas_asignadas = []
                    for escolta in self.escoltas:
                        if len(escoltas_asignadas) < escoltas_necesarias:
                            escoltas_asignadas.append(escolta)
                    return {
                        'vehiculo': vehiculo,
                        'escoltas': escoltas_asignadas,
                        'pedido': pedido
                    }
        return None

    def calcular_ruta_optima(self, v_inicial, v_final):
        distancias = self.ciudad.djk(v_inicial)
        ruta = [v_final]
        while v_final != v_inicial:
            for v in self.ciudad.grafo.neighbors(v_final):
                if distancias[v] + self.ciudad.grafo[v][v_final]['peso'] == distancias[v_final]:
                    ruta.append(v)
                    v_final = v
                    break
        ruta.reverse()
        return ruta
    
    def start_simulation(self):
        threading.Thread(target=self.run_simulation).start()

    def run_simulation(self):
        while self.pedidos:
            asignacion = self.asignar_vehiculos_y_escoltas()
            if asignacion:
                ruta = self.calcular_ruta_optima(asignacion['pedido']['origen'], asignacion['pedido']['destino'])
                tiempo_total = asignacion['vehiculo'].mover(ruta, nx.get_edge_attributes(self.ciudad.grafo, 'peso'))
                print(f"Vehículo {asignacion['vehiculo'].tipo} completó el pedido en {tiempo_total} segundos")
                time.sleep(tiempo_total)  # Simular el tiempo de entrega
        print("Todos los pedidos han sido completados")


    def attack(self):
        pass
