# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
<<<<<<< HEAD
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
=======
from reportlab.lib.units import inch
>>>>>>> 7209367c4e42dc5ec14b6dec370d9842d10cf38f

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
<<<<<<< HEAD
titulo = "Cartorio Sumaré"
=======
Titulo = "Cartorio Sumaré"
>>>>>>> 7209367c4e42dc5ec14b6dec370d9842d10cf38f
subtitulo = "Relatorio Mensal"
pageinfo = "platypus example"

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
<<<<<<< HEAD
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, titulo)
    canvas.setFont('Times-Bold',12)
    canvas.drawCentredString(PAGE_WIDTH/2.0,PAGE_HEIGHT-125,subtitulo)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(2.5*cm, 2 * cm,"Página 1")
=======
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Titulo)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch,"First Page / %s" % pageinfo)
>>>>>>> 7209367c4e42dc5ec14b6dec370d9842d10cf38f
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
<<<<<<< HEAD
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
=======
    canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def go():
    doc = SimpleDocTemplate("phello.pdf")
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]
    for i in range(10):
        bogustext = ("Paragraph number %s. " % i) + ("Teste paragrafo %s." % i)
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
>>>>>>> 7209367c4e42dc5ec14b6dec370d9842d10cf38f
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

if __name__ == "__main__":
    go()
