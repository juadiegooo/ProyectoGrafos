from src.view import View
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = View()
    app.exec_()
