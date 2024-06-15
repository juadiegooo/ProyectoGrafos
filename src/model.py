import networkx as nx

#Nos ayuda a todo lo relacionado con la ciudad
class Ciudad:
    def __init__(self):
        self.grafo = nx.Graph()

    #funciones para agregar los nodos principales al grafo
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
    
    def djk(self, v_inicial):
        distancias = {v: float('inf') for v in self.grafo.nodes}
        distancias[v_inicial] = 0
        visitados = set()
        cola = [(0, v_inicial)]
        while cola:
            d_act, v_act = min(cola)
            cola.remove((d_act, v_act))
            if v_act not in visitados:
                visitados.add(v_act)
                for ady in self.grafo.neighbors(v_act):
                    peso = self.grafo[v_act][ady]['peso']
                    nueva_dist = d_act + peso
                    if nueva_dist < distancias[ady]:
                        distancias[ady] = nueva_dist
                        cola.append((nueva_dist, ady))
        return distancias

class Vehiculo:
    def __init__(self, tipo, capacidad, escudo, ataque, escoltas_necesarias):
        self.tipo = tipo
        self.capacidad = capacidad
        self.escudo = escudo
        self.ataque = ataque
        self.escoltas_necesarias = escoltas_necesarias
        
    def mover(self, ruta, tiempo_por_arista):
        tiempo_total = 0
        for i in range(len(ruta) - 1):
            tiempo_total += tiempo_por_arista[(ruta[i], ruta[i+1])]
        return tiempo_total

class Escolta:
    def __init__(self, escudo, ataque):
        self.escudo = escudo
        self.ataque = ataque
