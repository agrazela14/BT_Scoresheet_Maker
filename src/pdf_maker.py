from reportlab.pdfgen        import canvas
from reportlab.lib.units     import inch
from reportlab.lib.pagesizes import A4

# Process:
# First determine player count, and horizontally divide the page to give each player even space
# Second determine the the number of objectives and largest number of units among players, then divide the page vertically in a ratio between the two
# Based on how the page is divided, determine a suitable font size and entry box size to fill it out

def hello(c):
    for x in range (8):
        for y in range (11):
            c.drawString(x * inch, y * inch, str(x) + " in, " + str(y) + " up")

c = canvas.Canvas("Hello.pdf", A4)
hello(c)
c.showPage()
c.save()
