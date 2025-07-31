from reportlab.pdfgen        import canvas
from reportlab.lib.units     import inch
from reportlab.lib.pagesizes import A4
import InputGui

# Process:
# First determine player count, and horizontally divide the page to give each player even space
# Second determine the the number of objectives and largest number of units among players, then divide the page vertically in a ratio between the two
# Based on how the page is divided, determine a suitable font size and entry box size to fill it out

# We need to take the data in from the input_gui, process it, then build the pdf

class PdfBuilder:
    # Using hold onto the dataclasses here
    data_list     : list
    player_data   : list
    objective_data: list
    unit_data     : list

    def __init__(self):
        print("init pdfBuilder")

    def build_pdf(self, data_list):
        # Recieve the data from the InputGui, then call a processing function, then with the output of that call a pdf building function
        print("Got to the build pdf function")
        self.data_list = data_list
        self.process_data()
        self.check_data()
        #self.draw_pdf()
        #print("Passed DrawPDF")

    def process_data(self):
        # iterate though the 3 lists in the data_list
        self.player_data    = self.data_list[0]
        self.objective_data = self.data_list[1]
        self.unit_data      = self.data_list[2]
    
    # A function to look at what we recieved in from gui 
    def check_data(self):
        print("Checking received data")
        for player in self.player_data:
            print("player name:" + player.player_name)
            print("player faction:" + player.player_faction)
            print("player number:" + str(player.player_number))

        for obj in self.objective_data:
            print(obj.objective_name)
            print(obj.objective_type)
            print(obj.objective_value)

        for unit in self.unit_data:
            print(unit.unit_name)
            print(unit.unit_bv)
            print(unit.unit_gunnery)
            print(unit.unit_piloting)
            print(unit.unit_owner)
        

    def player_units(self):
        player_unit_counts = []
        for unit in self.unit_data:
            if (player_unit_counts.len() <= unit.unit_owner):
                player_unit_counts.append(1)
            else:
                player_unit_counts[unit.unit_owner] += 1
        return player_unit_counts
                
 
#    def draw_pdf(self):
#        #more drawing test
#        #c.drawString(4 * inch, 5 * inch, "Draw Complete, 4 inches in, 5 inches up")
#        #c.showPage()
#        #c.save()
#        # Use report lab along with the data put into the class variables to draw the pdf
#        c = canvas.Canvas("Out.pdf", A4)
#
#        # find the player with the most units
#        player_units = self.most_units(self)
#        most_units   = max(player_units)
#        # Give each player an equal section of the width of the 8.5" page
#        column_width = inch * (8.5 / self.player_data.len())
#        # For each value in each data class, plus 1 for each unit from the player with the most units, give an inch of space
#        row_count   = inch * (11 / ( (self.player_data.len() * 3) + (self.objective_data.len() * 3) + (most_units) )
#        
#        self.draw_players(self, c, column_width, row_count)
#        self.draw_objectives(self, c, column_width, row_count) 
#        self.draw_units(self, c, column_width, row_count, player_units)
#    
#    def draw_players(self, c, column_width, row_count):
#        for player in self.player_data:
#            c.drawString( column_width * (player.player_number - 1), row_count, player.player_name) 
#            c.drawString( column_width * (player.player_number - 1), row_count - 1, player.player_faction) 
#            c.drawString( column_width * (player.player_number - 1), row_count - 2, player.player_faction) 
#
#
#    def draw_objectives(self, c, column_width, row_count):
#        for obj in self.objective_data:
#            for x in range(0, self.player_data.len()):
#                c.drawString( column_width * (x), row_count - 3, obj.objective_name) 
#                c.drawString( column_width * (x), row_count - 4, obj.objective_type) 
#                c.drawString( column_width * (x), row_count - 5, obj.objective_value)) 
#        
#    def draw_units(self, c, column_width, row_count, player_units):
#        # Start by just drawing the unit name 
#        utilized_units = [0] * player_units.len()
#        for unit in self.unit_data:
#            c.drawString( column_width * unit.unit_owner, row_count - (6 + utilized_units[unit.unit_owner - 1]), unit.unit_name)
#            utilized_units[unit._unit_owner - 1] += 1 
           

# reportlab test code
#def hello(c):
#    for x in range (8):
#        for y in range (11):
#            c.drawString(x * inch, y * inch, str(x) + " in, " + str(y) + " up")
#
#c = canvas.Canvas("Hello.pdf", A4)
#hello(c)
#c.showPage()
#c.save()
