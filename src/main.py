import input_gui
import pdf_builder
import sys
import random
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = input_gui.AppGui()
    widget.resize(800, 800)
    widget.show()

    sys.exit(app.exec())
