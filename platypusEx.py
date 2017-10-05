# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
titulo = "Cartorio Sumaré"
subtitulo = "Relatorio Mensal"
pageinfo = "platypus example"

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, titulo)
    canvas.setFont('Times-Bold',12)
    canvas.drawCentredString(PAGE_WIDTH/2.0,PAGE_HEIGHT-125,subtitulo)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(2.5*cm, 2 * cm,"Página 1")
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(2.5*cm, 2 * cm,"Página %d" % (doc.page))
    canvas.restoreState()

def go():
    doc = SimpleDocTemplate("Relatorio Mensal.pdf",pagesize=A4)
    Story = [Spacer(0.5*cm,3.1*cm)]
    style = styles["Normal"]
    cabecalho = ("Id") + ("nome do Cliente") + ("RG do Cliente") + ("CPF do Cliente") + ("Data Registro")
    cabecalho = Paragraph(cabecalho,style)
    Story.append(cabecalho)
    Story.append(Spacer(1*cm,0.4*cm))
    for i in range(48):
        bogustext = ("Id %s. " % i) + ("Nome do Cliente %s." % i)+ ("RG %s." % i) + ("CPF %s." % i) + ("Data Registro %s." % i)
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1*cm,0.4*cm))
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

if __name__ == "__main__":
    go()
