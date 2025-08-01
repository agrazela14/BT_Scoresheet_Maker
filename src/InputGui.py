import PdfBuilder 
from dataclasses import dataclass
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui

#TODO: 
#   Work on getting the data contained in the GUI Fields out to the PDF Reporter
#   Add a remove entry button to each entry (This would of course also have to remove the underlying data)
#   IMPORTANT: Need to add callbacks to fill out the data lists when a box is interacted with, or when make pdf is pressed

@dataclass
class PlayerData:
    player_name:    str
    player_faction: str 
    player_number:  int
    index:          int
    
    def __init__(self, 
                 player_name:    str, 
                 player_faction: str,
                 player_number:  int, 
                 index:          int):

        self.player_name    = player_name
        self.player_faction = player_faction
        self.player_number  = player_number
        self.index          = index 
    
    def set_player_name(self, player_name):
        self.player_name = player_name

    def set_player_faction(self, player_name):
        self.player_faction = player_faction
        
    def set_player_number(self, player_number):
        self.player_number = player_number

@dataclass
class ObjectiveData:
    objective_name:  str
    objective_type:  str 
    objective_value: int
    index:           int
    def __init__(self, 
                 objective_name:  str, 
                 objective_type:  str,
                 objective_value: int, 
                 index:           int):

        self.objective_name  = objective_name
        self.objective_type  = objective_type
        self.objective_value = objective_value
        self.index           = index 

    def set_objective_name(self, objective_name):
        self.objective_name = objective_name

    def set_objective_type(self, objective_type):
        self.objective_type = objective_type
        
    def set_objective_value(self, objective_value):
        self.objective_value = objective_value

@dataclass
class UnitData:
    unit_name:     str
    unit_bv:       str 
    unit_gunnery:  int
    unit_piloting: int
    unit_owner:    int
    index:         int
    def __init__(self, 
                 unit_name:     str, 
                 unit_bv:       str,
                 unit_gunnery:  int, 
                 unit_piloting: int, 
                 unit_owner:    int, 
                 index:         int):

        self.unit_name     = unit_name 
        self.unit_bv       = unit_bv 
        self.unit_gunnery  = unit_gunnery 
        self.unit_piloting = unit_piloting 
        self.unit_owner    = unit_owner
        self.index         = index 

class PlayerSection():
    # A list of player dataclass objects containing the entered data
    player_data         : list    
    # holds the HBox layouts which contain the input form
    player_vlayout      : QtWidgets.QVBoxLayout 
    player_count        : int
    player_name_list    : list
    player_faction_list : list
    player_number_list  : list
    
    def __init__(self):
        self.player_vlayout      = QtWidgets.QVBoxLayout() 
        self.player_data         = []
        self.player_count        = 0
        self.player_name_list    = []
        self.player_faction_list = []
        self.player_number_list  = []

    def get_player_data(self):
        for entry in range(0, self.player_count):
            self.player_data.append(PlayerData(self.player_name_list[entry].text(), 
                                               self.player_faction_list[entry].text(), 
                                               self.player_number_list[entry].currentText(), 
                                               entry))
        return self.player_data 

    def wipe_player_data(self):
        self.player_data = []

    def add_player_callback(self):
        # Called by the parent class's callback, adds the HBox and data to player_vlayout and player_data respectively
        new_player            = QtWidgets.QHBoxLayout()
        player_number_layout  = QtWidgets.QHBoxLayout()
        player_number_counter = QtWidgets.QComboBox()
        player_name           = QtWidgets.QLineEdit()
        player_faction        = QtWidgets.QLineEdit()

        player_number_counter.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        player_number_counter.setFrame( True )

        player_number_layout.addWidget(QtWidgets.QLabel("Player Number"))
        player_number_layout.addWidget(player_number_counter)

        player_name.setPlaceholderText("Player Name")
        player_faction.setPlaceholderText("Player Faction")

        new_player.addWidget(player_name)
        new_player.addWidget(player_faction)
        new_player.addLayout(player_number_layout)

        self.player_number_list.append(player_number_counter)
        self.player_name_list.append(player_name)
        self.player_faction_list.append(player_faction)

        self.player_vlayout.addLayout(new_player)
        self.player_count += 1
    
    def get_player_layout(self):
        return self.player_vlayout

class ObjectiveSection():
    # A list of player dataclass objects containing the entered data
    objective_data         : list    
    # holds the HBox layouts which contain the input form
    objective_vlayout      : QtWidgets.QVBoxLayout 
    objective_count        : int
    objective_name_list    : list
    objective_type_list    : list
    objective_value_list   : list
    
    def __init__(self):
        self.objective_vlayout    = QtWidgets.QVBoxLayout() 
        self.objective_data       = []
        self.objective_count      = 0
        self.objective_name_list  = [] 
        self.objective_type_list  = [] 
        self.objective_value_list = [] 

    def get_objective_data(self):
        for entry in range(0, self.objective_count):
            self.objective_data.append(ObjectiveData(self.objective_name_list[entry].text(), 
                                                     self.objective_type_list[entry].text(), 
                                                     self.objective_value_list[entry].text(), 
                                                     entry))
        return self.objective_data 

    def wipe_objective_data(self):
        self.objective_data = []

    # TODO input validation, or do that in the change callback for the QLineEdits
    def add_objective_callback(self):
        # Called by the parent class's callback, adds the HBox and data to objective_vlayout and objective_data respectively
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

        self.objective_name_list.append(objective_name)
        self.objective_type_list.append(objective_type)
        self.objective_value_list.append(objective_value)

        self.objective_vlayout.addLayout(new_objective)

        self.objective_count += 1

    def get_objective_layout(self):
        return self.objective_vlayout

class UnitSection():
    # A list of player dataclass objects containing the entered data
    unit_data          : list    
    # holds the HBox layouts which contain the input form
    unit_vlayout       : QtWidgets.QVBoxLayout 
    unit_count         : int
    unit_name_list     : list
    unit_bv_list       : list
    unit_gunnery_list  : list
    unit_piloting_list : list
    unit_owner_list    : list
    
    def __init__(self):
        self.unit_vlayout       = QtWidgets.QVBoxLayout() 
        self.unit_data          = []
        self.unit_count         = 0 
        self.unit_name_list     = [] 
        self.unit_bv_list       = [] 
        self.unit_gunnery_list  = [] 
        self.unit_piloting_list = [] 
        self.unit_owner_list    = [] 

    def wipe_unit_data(self):
        self.unit_data = []

    def get_unit_data(self):
        for entry in range(0, self.unit_count):
            self.unit_data.append(UnitData(self.unit_name_list[entry].text(), 
                                           self.unit_bv_list[entry].text(), 
                                           self.unit_gunnery_list[entry].currentText(), 
                                           self.unit_piloting_list[entry].currentText(), 
                                           self.unit_owner_list[entry].currentText(), 
                                           entry))
        return self.unit_data

    def add_unit_callback(self):
        # Called by the parent class's callback, adds the HBox and data to unit_vlayout and unit_data respectively
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

        self.unit_name_list.append(unit_name)
        self.unit_bv_list.append(unit_bv)
        self.unit_gunnery_list.append(unit_gunnery)
        self.unit_piloting_list.append(unit_piloting)
        self.unit_owner_list.append(owner_number_counter)

        self.unit_vlayout.addLayout(new_unit)
        self.unit_count += 1

    def get_unit_layout(self):
        return self.unit_vlayout

         
class InputGui(QtWidgets.QWidget):
    parent_layout        : QtWidgets.QVBoxLayout
    players              : PlayerSection
    objectives           : ObjectiveSection
    units                : UnitSection
    add_player_button    : QtWidgets.QPushButton
    add_objective_button : QtWidgets.QPushButton
    add_unit_button      : QtWidgets.QPushButton
    make_pdf_button      : QtWidgets.QPushButton

    def __init__(self):
        super().__init__()
        # Graphical Objects Initialization
        self.parent_layout = QtWidgets.QVBoxLayout(self)
        
        self.players    = PlayerSection()
        self.objectives = ObjectiveSection()
        self.units      = UnitSection()

        self.add_player_button    = QtWidgets.QPushButton("Add Player")
        self.add_objective_button = QtWidgets.QPushButton("Add Objective")
        self.add_unit_button      = QtWidgets.QPushButton("Add Unit")
        self.make_pdf_button      = QtWidgets.QPushButton("Make PDF")
        
        self.parent_layout.addWidget(self.add_player_button) 
        self.parent_layout.addLayout(self.players.get_player_layout()) 

        self.parent_layout.addWidget(self.add_objective_button) 
        self.parent_layout.addLayout(self.objectives.get_objective_layout()) 

        self.parent_layout.addWidget(self.add_unit_button) 
        self.parent_layout.addLayout(self.units.get_unit_layout()) 

        self.parent_layout.addWidget(self.make_pdf_button)
        
        self.add_player_button.clicked.connect(self.add_player)
        self.add_objective_button.clicked.connect(self.add_objective)
        self.add_unit_button.clicked.connect(self.add_unit)
        self.make_pdf_button.clicked.connect(self.make_pdf)

    def add_player(self): 
        self.players.add_player_callback()

    def add_objective(self): 
        self.objectives.add_objective_callback()

    def add_unit(self): 
        self.units.add_unit_callback()

    # Return a datastructure containing the information entered in the fields above
    # Probably a list of dataclasses for each of the items (player, objective, unit)

    def make_pdf(self):
        # Assemble the entry data from the sections and pass it off to a callback in the pdf maker program 
        # Call functions in each of the child objects that return a list of their data
        builder    = PdfBuilder.PdfBuilder()
        players    = self.players.get_player_data()
        objectives = self.objectives.get_objective_data()
        units      = self.units.get_unit_data()

        full_data  = [players, objectives, units]

        # send a list of lists to the pdf maker in the order of [players, objectives, units]
        builder.build_pdf(full_data)

        # Wipe out the data after sending it, so that it doesn't pile up with repeated makes
        self.players.wipe_player_data()
        self.objectives.wipe_objective_data()
        self.units.wipe_unit_data()
