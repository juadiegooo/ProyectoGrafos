import networkx as nx

class CentroOperacion:
    def __init__(self, capacidad_dinero, capacidad_vehiculos, capacidad_escoltas):
        self.capacidad_dinero = capacidad_dinero
        self.capacidad_vehiculos = capacidad_vehiculos
        self.capacidad_escoltas = capacidad_escoltas
        self.dinero_actual = 0
        self.vehiculos = []
        self.escoltas = []

class Cliente:
    def __init__(self, nombre, dinero_a_transportar, tiempo_entrega):
        self.nombre = nombre
        self.dinero_a_transportar = dinero_a_transportar
        self.tiempo_entrega = tiempo_entrega

class Vehiculo:
    def __init__(self, tipo, velocidad, capacidad, escudo, ataque, escoltas_necesarias):
        self.tipo = tipo
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.escudo = escudo
        self.ataque = ataque
        self.escoltas_necesarias = escoltas_necesarias

class Escolta:
    def __init__(self, escudo, ataque):
        self.escudo = escudo
        self.ataque = ataque

class Puente:
    def __init__(self, capacidad):
        self.capacidad = capacidad

class Ladron:
    def __init__(self, escudo, ataque):
        self.escudo = escudo
        self.ataque = ataque

class Ciudad:
    def __init__(self):
        self.grafo = nx.Graph()
    
    def agregar_centro_operacion(self, id, capacidad_dinero, capacidad_vehiculos, capacidad_escoltas):
        self.grafo.add_node(id, tipo='centro_operacion', capacidad_dinero=capacidad_dinero,
                            capacidad_vehiculos=capacidad_vehiculos, capacidad_escoltas=capacidad_escoltas)

    def agregar_cliente(self, id, nombre, dinero_a_transportar, tiempo_entrega):
        self.grafo.add_node(id, tipo='cliente', nombre=nombre, dinero_a_transportar=dinero_a_transportar,
                            tiempo_entrega=tiempo_entrega)

    def agregar_puente(self, id, capacidad):
        self.grafo.add_node(id, tipo='puente', capacidad=capacidad)

    def agregar_ruta(self, id1, id2, peso):
        self.grafo.add_edge(id1, id2, peso=peso)

    def obtener_grafo(self):
        return self.grafo
