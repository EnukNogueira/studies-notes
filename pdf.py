import pydf

pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('meuarquivo.pdf', 'wb') as arquivo:
    arquivo.write(pdf)