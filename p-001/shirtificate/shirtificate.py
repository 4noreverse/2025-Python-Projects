from fpdf import FPDF

class Shirt:
    def __init__(self, name):
        self.name = name + ' took CS50'

    def shirty(self):
        pdf = FPDF(orientation='portrait', format='A4')
        pdf.set_text_color(255, 255, 255)
        pdf.add_page(orientation = 'P')
        #pdf.set_page_background('shirtificate.png')
        img_w = 180
        img_h = 120
        x = (pdf.w - img_w) / 2
        y = 50
        pdf.image('shirtificate.png', x = x, y = y, w = img_w, h = img_h, keep_aspect_ratio = True)
        pdf.set_y(85)
        pdf.set_font('Times', size = 20, style = 'I')
        pdf.set_x(0)
        pdf.cell(w = pdf.w, text = self.name, align = 'C')
        pdf.output('shirtificate.pdf')

student_name = input('Name: ')
shirt = Shirt(student_name)
shirt.shirty()
