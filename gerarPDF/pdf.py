from reportlab.pdfgen import canvas


def generate_pdf(lista):
    try:
        nome_pdf = input('Informe o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome, idade in lista.items():
            x -= 20
            pdf.drawString(247, x, '{} : {}'.format(nome, idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont('Helvetica-Oblique', 14)
        pdf.drawString(245, 750, 'Lista de Clientes')
        pdf.setFont('Helvetica-Oblique', 12)
        pdf.drawString(245, 724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))


lista = {'Felipe': '24', 'Renan': '29',
         'Jose': '42', 'Maria': '22', 'Eduardo': '31'}

generate_pdf(lista)
