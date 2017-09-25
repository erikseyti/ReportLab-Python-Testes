'''
    Classe criada para testar o recurso ReportLab
    em Python
'''
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
import csv
from reportlab.pdfgen import canvas



data_file = 'data.csv'


def import_data(data_file):
    ateendee_data = csv.reader(open(data_file,"rb"))
    for row in ateendee_data:
        sobrenome = row[0]
        nome = row[1]
        curso = row[2]
        nome_pdf = curso + " "+ nome + " " +sobrenome + ".pdf"
        generate_certificate(nome,sobrenome,curso,nome_pdf)

def generate_certificate(nome,sobrenome,curso,nome_pdf):
    nome_extenso = nome+" "+ sobrenome
    c = canvas.Canvas(nome_pdf,pagesize=landscape(letter))

    #header do pdf
    c.setFont('Helvetica',48,leading = None)
    c.drawCentredString(415,500,"Certificado de Conclusão:")
    c.setFont('Helvetica',24,leading = None)
    c.drawCentredString(415,450,'Este Certificado Vai Para:')
    # nome da pessoa no pdf
    c.drawCentredString('Helvetica',34,leading = None)
    c.drawCentredString(415,395,nome_extenso)
    #por completar o curso:
    c.setFont('Helvetica',24,leading = None)
    c.drawCentredString(415,350,"Por Completar o Curso:")
    #nome do curso
    c.setFont("Helvetica",20,leading = None)
    c.drawCentredString(415,310,curso)
    #imagem de teste
    ex = "exemplo_etc.png"
    c.drawImage(ex,350,50,width=None,height=None)

    c.showPage()
    c.save()

import_data(data_file)
