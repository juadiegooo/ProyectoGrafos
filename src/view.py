from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget
import matplotlib.pyplot as plt
import networkx as nx
from .controller import Controller

class View(QtWidgets.QMainWindow):
    def __init__(self):
        super(View, self).__init__()
        self.controller = Controller(self)
        self.initUI()
        self.mostrar_grafo()

    def initUI(self):
        self.setWindowTitle('Simulación de Ciudad')
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        self.attack_button = QPushButton('Asalto')
        self.attack_button.clicked.connect(self.controller.attack)
        layout.addWidget(self.attack_button)

        central_widget.setLayout(layout)
        self.show()

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
