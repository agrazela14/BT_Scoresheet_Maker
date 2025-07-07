import sys
import random
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui

class AppWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
    
        self.parent_layout     = QtWidgets.QVBoxLayout(self)
        self.units_layout      = QtWidgets.QVBoxLayout()
        self.objectives_layout = QtWidgets.QVBoxLayout()

        self.parent_layout.addLayout(self.units_layout)
        self.parent_layout.addLayout(self.objectives_layout)
    # Create the parent widget, including a VBoxLayout that holds the other layouts
    # addLayout to add a Players, Objectives, Units, Scoring, HBoxLayouts


    # Include an Add button to add a new unit, each unit is represented by text boxes
    # [Unit Name, Unit BV, Unit Skill] for each unit

        self.add_unit_button = QtWidgets.QPushButton("Add Unit")
        self.add_unit_button.clicked.connect(self.add_unit)
        self.units_layout.addWidget(self.add_unit_button)



#    def add_objective(QLayout parent): 
    def add_unit(parent):
        new_unit = QtWidgets.QHBoxLayout()

        new_unit.addWidget(QtWidgets.QLineEdit("Unit Name"))
        new_unit.addWidget(QtWidgets.QLineEdit("Unit BV"))
        new_unit.addWidget(QtWidgets.QLineEdit("Unit Skill"))

        parent.units_layout.addLayout(new_unit)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = AppWindow()
    widget.resize(800, 800)
    widget.show()

    sys.exit(app.exec())
