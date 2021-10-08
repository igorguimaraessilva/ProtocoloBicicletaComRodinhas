from reportlab.pdfgen import canvas

def GeneratePDF(lista):
    try :
        
        nome_pdf = input('Informe o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        
        for nome,data in lista.items():
            
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome,data))
        
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)    
        #pdf.drawString(247,700, 'nome e data')
        pdf.setFont("Helvetica-Bold", 12)
        #pdf.drawString(245,724, 'Nome e data')
        pdf.save()
        print('{}.pdf criado com suceso!'.format(nome_pdf))
    except :
        print('Erro ao gerar {}.pdf'.format(nome_pdf))

lista = {'ESCREVA SEU ASSUNTO': '04/10/2021'}

GeneratePDF(lista)
