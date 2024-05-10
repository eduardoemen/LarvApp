from reportlab.pdfgen import canvas
img_file = '1.jpg'
pdf_file = 'reporte.pdf'
 
can = canvas.Canvas(pdf_file)
can.drawString(20, 400,"este es el reporte del trabajo realizado" )
 
x_start = 0
y_start = 0
can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
 
can.showPage()
can.save()
