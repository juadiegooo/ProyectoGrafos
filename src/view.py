import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLabel
import matplotlib.pyplot as plt
import networkx as nx
from controller import Controller
#Actualizamos los imports para las animaciones
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
sys.path.append('./src')

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
        
        self.ruta_button = QPushButton('Calcular Ruta')
        self.ruta_button.clicked.connect(self.calcular_ruta)
        layout.addWidget(self.ruta_button)

        self.ruta_label = QLabel('')
        layout.addWidget(self.ruta_label)
        
        self.animar_button = QPushButton('Animar Vehículo')
        self.animar_button.clicked.connect(self.animar_vehiculo)
        layout.addWidget(self.animar_button)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        central_widget.setLayout(layout)
        self.show()

    def mostrar_grafo(self):
        self.grafo = self.controller.ciudad.obtener_grafo()
        self.pos = nx.spring_layout(self.grafo)  # Posiciones para todos los nodos

        ax = self.figure.add_subplot(111)
        ax.clear()

        # Dibujar nodos con diferentes colores por tipo
        tipos = nx.get_node_attributes(self.grafo, 'tipo')
        colores = {'centro_operacion': 'red', 'cliente': 'blue', 'puente': 'green'}
        node_colors = [colores[tipos[nodo]] for nodo in self.grafo.nodes]

        nx.draw(self.grafo, self.pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, ax=ax)
        labels = nx.get_edge_attributes(self.grafo, 'peso')
        nx.draw_networkx_edge_labels(self.grafo, self.pos, edge_labels=labels, ax=ax)

        self.canvas.draw()
    
    def calcular_ruta(self):
        distancias = self.controller.calcular_ruta_optima(1)
        ruta_texto = 'Distancias desde el nodo 1:\n'
        for nodo, distancia in distancias.items():
            ruta_texto += f'{nodo}: {distancia}\n'
        self.ruta_label.setText(ruta_texto)
    
    #Metodo para animar la ruta
    def animar_vehiculo(self):
        ax = self.figure.add_subplot(111)
        ax.clear()

        nx.draw(self.grafo, self.pos, with_labels=True, ax=ax, node_size=500)

        # Ruta de ejemplo para animación
        ruta = [1, 3, 4, 5]

        def update(num):
            ax.clear()
            nx.draw(self.grafo, self.pos, with_labels=True, ax=ax, node_size=500)
            if num < len(ruta) - 1:
                nx.draw_networkx_edges(self.grafo, self.pos, edgelist=[(ruta[num], ruta[num+1])], width=2.5, alpha=0.6, edge_color='r')
            self.canvas.draw()

        self.ani = FuncAnimation(self.figure, update, frames=len(ruta), interval=1000, repeat=False)
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = View()
    app.exec_()
