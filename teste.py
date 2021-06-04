from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("hello.pdf", pagesize=A4)

# auto generated elements
texto = c.drawString(1*cm, 2*cm, "Teste 1")
texto = c.drawString(30, 200, "Segunda frase")
texto = c.drawString(50, 400, "Terceira frase")
texto = c.drawString(80, 600, "Esta frase contêm acentos.")
texto = c.drawString(150, 800, "Teste: #$#$(#$*@*%@#L$PTOI$). Ok")

# Save
c.showPage()
c.save()
