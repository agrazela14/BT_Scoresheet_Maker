import sys
import random
from dataclasses import dataclass
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui

@dataclass
class Player:
    player_name:    str
    player_faction: str 
    player_number:  int

@dataclass
class Objective:
    objective_name:  str
    objective_type:  str 
    objective_value: int

@dataclass
class Unit:
    unit_name:     str
    unit_bv:       str 
    unit_gunnery:  int
    unit_piloting: int

class AppGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.parent_layout     = QtWidgets.QVBoxLayout(self)
        self.players_layout    = QtWidgets.QVBoxLayout()
        self.objectives_layout = QtWidgets.QVBoxLayout()
        self.units_layout      = QtWidgets.QVBoxLayout()
        self.make_pdf_button   = QtWidgets.QPushButton("Make PDF")

        self.parent_layout.addLayout(self.players_layout)
        self.parent_layout.addLayout(self.objectives_layout)
        self.parent_layout.addLayout(self.units_layout)
        self.parent_layout.addWidget(self.make_pdf_button)
        # Create the parent widget, including a VBoxLayout that holds the other layouts
        # addLayout to add a Players, Objectives, Units, Scoring, HBoxLayouts


        # Include an Add button to add a new unit, each unit is represented by text boxes
        # [Unit Name, Unit BV, Unit Skill] for each unit
        self.add_player_button = QtWidgets.QPushButton("Add Player")
        self.add_player_button.clicked.connect(self.add_player)
        self.players_layout.addWidget(self.add_player_button)

        self.add_objective_button = QtWidgets.QPushButton("Add Objective")
        self.add_objective_button.clicked.connect(self.add_objective)
        self.objectives_layout.addWidget(self.add_objective_button)

        self.add_unit_button = QtWidgets.QPushButton("Add Unit")
        self.add_unit_button.clicked.connect(self.add_unit)
        self.units_layout.addWidget(self.add_unit_button)

        self.make_pdf_button.clicked.connect(self.make_pdf)



    # TODO: make the Player number a dropdown with numbers
    #       The layout containing the dropdown and it's label has way too much spacing between the two
    def add_player(self): 
        new_player            = QtWidgets.QHBoxLayout()
        player_number_layout  = QtWidgets.QHBoxLayout()
        player_number_counter = QtWidgets.QComboBox()

        player_number_counter.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        player_number_counter.setFrame( True )

        player_number_layout.addWidget(QtWidgets.QLabel("Player Number"))
        player_number_layout.addWidget(player_number_counter)
        player_number_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)

        new_player.addWidget(QtWidgets.QLineEdit("Player Name"))
        new_player.addWidget(QtWidgets.QLineEdit("Player Faction"))
        new_player.addLayout(player_number_layout)

        self.players_layout.addLayout(new_player)

    def add_objective(self): 
        new_objective   = QtWidgets.QHBoxLayout()
        objective_name  = QtWidgets.QLineEdit()
        objective_type  = QtWidgets.QLineEdit()
        objective_value = QtWidgets.QLineEdit()

        objective_name.setPlaceholderText("Objective Name")
        objective_type.setPlaceholderText("Objective Type (Primary, Secondary, etc...")
        objective_value.setPlaceholderText("Objective Value")

        new_objective.addWidget(objective_name)
        new_objective.addWidget(objective_type)
        new_objective.addWidget(objective_value)

        self.objectives_layout.addLayout(new_objective)

    # TODO: make the owning player a dropdown with numbers
    def add_unit(self):
        new_unit             = QtWidgets.QHBoxLayout()
        owner_number_layout  = QtWidgets.QHBoxLayout()
        owner_number_counter = QtWidgets.QComboBox()
        unit_name            = QtWidgets.QLineEdit()
        unit_bv              = QtWidgets.QLineEdit()
        unit_skill_layout    = QtWidgets.QHBoxLayout()
        unit_gunnery         = QtWidgets.QComboBox()
        unit_piloting        = QtWidgets.QComboBox()
        

        owner_number_counter.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        owner_number_counter.setFrame( True )

        owner_number_layout.addWidget(QtWidgets.QLabel("Owner Number"))
        owner_number_layout.addWidget(owner_number_counter)

        unit_name.setPlaceholderText("Unit Name")
        unit_bv.setPlaceholderText("Unit BV")
        
        unit_gunnery.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        unit_gunnery.setCurrentIndex(4)

        unit_piloting.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        unit_piloting.setCurrentIndex(5)
        
        unit_skill_layout.addWidget(QtWidgets.QLabel("Gunnery"))
        unit_skill_layout.addWidget(unit_gunnery)
        unit_skill_layout.addWidget(QtWidgets.QLabel("Piloting"))
        unit_skill_layout.addWidget(unit_piloting)
        

        new_unit.addWidget(unit_name)
        new_unit.addWidget(unit_bv)
        new_unit.addLayout(unit_skill_layout)
        new_unit.addLayout(owner_number_layout)

        self.units_layout.addLayout(new_unit)

    # Return a datastructure containing the information entered in the fields above
    # Probably a list of dataclasses for each of the items (player, objective, unit)
    def make_pdf(self):
        print("This will create the pdf based on the inputted data")
        

