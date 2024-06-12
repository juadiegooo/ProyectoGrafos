from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import networkx as nx
from controller import controller

class View(QtWidgets.QMainWindow):
    def __init__(self):
        super(View, self).__init__()
        uic.loadUi('main.ui', self)
        self.controller = controller(self)
        self.attack_button.clicked.connect(self.controller.attack)
        self.show()
        self.mostrar_grafo()

    def mostrar_grafo(self):
        grafo = self.controller.ciudad.obtener_grafo()
        pos = nx.spring_layout(grafo)  # Posiciones para todos los nodos

        # Dibujar nodos con diferentes colores por tipo
        tipos = nx.get_node_attributes(grafo, 'tipo')
        colores = {'centro_operacion': 'red', 'cliente': 'blue', 'puente': 'green'}
        node_colors = [colores[tipos[nodo]] for nodo in grafo.nodes]

        nx.draw(grafo, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10)
        labels = nx.get_edge_attributes(grafo, 'peso')
        nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)

        plt.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = View()
    app.exec_()
