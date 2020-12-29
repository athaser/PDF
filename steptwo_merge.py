# pdf_watermarker.py

from PyPDF2 import PdfFileWriter, PdfFileReader
from fpdf import FPDF
no=40
def create_watermark(u):
    lo = 1
   
    for t in range (no):
        watermark_obj = PdfFileReader("./stepone/OPS-000054 Mechanical Checklist Rev_C_E 8-{}.pdf".format(u))
        watermark_page = watermark_obj.getPage(0)
        lo += 1
    
    pdf_reader = PdfFileReader("./test.pdf")
    pdf_writer = PdfFileWriter()
        


    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        first_page = pdf_reader.getPage(0)
        page = pdf_reader.getPage(page)
        first_page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open("./steptwo/OPS-000054 Mechanical Checklist Rev_C_E 8-{}.pdf".format(u), 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
        for i in range(no):
            create_watermark(i)

print('end of loop')