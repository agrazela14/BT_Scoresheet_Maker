from reportlab.pdfgen        import canvas
from reportlab.lib.units     import inch
from reportlab.lib.pagesizes import A4
import input_gui

# Process:
# First determine player count, and horizontally divide the page to give each player even space
# Second determine the the number of objectives and largest number of units among players, then divide the page vertically in a ratio between the two
# Based on how the page is divided, determine a suitable font size and entry box size to fill it out

# We need to take the data in from the input_gui, process it, then build the pdf

class PdfBuilder:
    # Put the values from processing into these values
    player_data   : list
    objective_data: list
    unit_data     : list
    
    def __init__(self):
        print("init pdfBuilder")

    def BuildPdf(self, data_list):
        # Recieve the data from the input_gui, then call a processing function, then with the output of that call a pdf building function
        print("Got to the build pdf function")
        self.ProcessData(data_list)
        self.DrawPdf()
        print("Passed DrawPDF")
    
    def ProcessData(self, data_list):
        # iterate though the 3 lists in the data_list, pulling out the information and storing it in lists of primitives in the class
        return
 
    def DrawPdf(self):
        # Use report lab along with the data put into the class variables to draw the pdf
        c = canvas.Canvas("Test.pdf", A4)
        c.drawString(4 * inch, 5 * inch, "Draw Complete, 4 inches in, 5 inches up")
        c.showPage()
        c.save()

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
