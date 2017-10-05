from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

doc = SimpleDocTemplate("nome do arquivo.pdf", pagesize=letter)
c = canvas.Canvas("nome do arquivo.pdf", pagesize=letter)
texto = c.setFont('Helvetica',12,leading = None)
texto = c.drawCentredString(10.6*cm,27.5*cm,"Cartorio Sumaré")
texto = c.setFont('Helvetica',10,leading = None)
texto = c.drawString(6.8*cm,28.0*cm,"_______________________________________")
texto = c.drawString(6.8*cm,27.35*cm,"_______________________________________")
texto = c.drawCentredString(10.6*cm,26.5*cm,"Relatorio Mensal")

# container for the 'Flowable' objects
elements = []
c.showPage()
c.save()
data= [['nome1', 'tipo1', 'descricao1', 'data1', 'ativo1'],
       ['nome2', 'tipo2', 'descricao2', 'data2', 'ativo2'],
       ['nome3', 'tipo3', 'descricao3', 'data3', 'ativo3'],
       ['nome4', 'tipo4', 'descricao4', 'data4', 'ativo4']]
t=Table(data,5*[2*cm], 4*[2*cm])
# o 5 é considerado o numero de registros na linha, já o 4 refere-se ao numero de elementos cadastrados
t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('TEXTCOLOR',(0,0),(0,0),colors.red),
                       ('VALIGN',(0,0),(0,0),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))

elements.append(t)
# write the document to disk
doc.build(elements)
