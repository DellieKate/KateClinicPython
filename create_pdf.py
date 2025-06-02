from fpdf import FPDF

pdf = FPDF ()

pdf.add_page ()
pdf.set_font("Arial", size = 12)

#Header
pdf.cell(50, 10, txt="Full name", border=1, align="C")
pdf.cell(40, 10, txt="Birthday", border=1, align="C")
pdf.cell(35, 10, txt="Sex", border=1, align="C")
pdf.cell(60, 10, txt="Lab Recommendations", border=1, align="C")

#Patient rows
pdf.ln() 
pdf.cell(50, 10, txt="Kate Mendoza", border=1, align="C")
pdf.cell(40, 10, txt="01/01/1980", border=1, align="C")
pdf.cell(35, 10, txt="F", border=1, align="C")
pdf.cell(60, 10, txt="Lab Recommendations", border=1, align="C")
pdf.ln() 

pdf.output("Patient_File.pdf")

print("PDF created successfully.")