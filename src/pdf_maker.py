from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

def hello(c):
    for x in range (8):
        for y in range (11):
            c.drawString(x * inch, y * inch, str(x) + " in, " + str(y) + " up")

c = canvas.Canvas("Hello.pdf", A4)
hello(c)
c.showPage()
c.save()
