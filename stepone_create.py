from fpdf import FPDF

def multipage_simple(u):
    pdf = FPDF()
    pdf.set_font("Arial", size=11)
    pdf.add_page()
    line_no = 1
    for i in range (1): 
            pdf.cell(170, 111, txt="E 8/{}".format(u), ln=1, align="R")
            line_no += 1
    pdf.output("./stepone/OPS-000054 Mechanical Checklist Rev_C_E 8-{}.pdf".format(u))
   
       
if __name__ == '__main__':
    
    for j in range(40):
        multipage_simple(j)