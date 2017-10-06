# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1

from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

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
    tabela =[Spacer(width=0.5*cm,height=2.2*cm)]

    doc = SimpleDocTemplate("Relatorio Mensal.pdf",pagesize=A4)
    Story = []
    Story = [["ID", "Nome do Cliente", "RG", "CPF","Data Registro"],]
    for i in range(48):
        bogustext = ["id %s" % i,"nome %s"% i,"RG %s" % i, "CPF %s"% i,"data Registro %s" %i]
        Story.append(bogustext)
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                           ('VALIGN',(0,0),(0,-1),'TOP'),
                           ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                           ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),])
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(cell, s) for cell in row] for row in Story]
    t=Table(data2)
    t.setStyle(style)
    tabela.append(t)
    doc.build(tabela, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

if __name__ == "__main__":
    go()
