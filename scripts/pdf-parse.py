import io
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

#converts pdf, returns its text content as a string
def convert(fname, pages = None):
    pagenums = set() if not pages else set(pages)
    output = io.StringIO()

    pdf_manager = PDFResourceManager()
    text_converter = TextConverter(pdf_manager, output, laparams = LAParams())
    pdf_page_interpreter = PDFPageInterpreter(pdf_manager, text_converter)

    pdf_file = open(fname, 'rb')
    pages = PDFPage.get_pages(pdf_file, pagenums)

    for page in pages:
        pdf_page_interpreter.process_page(page)
    
    text = output.getvalue()

    output.close()
    pdf_file.close()
    text_converter.close()

    return text 

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 

    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        file_extension = pdf.split(".")[-1]

        if file_extension == "pdf":
            pdf_filename = pdfDir + pdf 
            
            text = convert(pdf_filename) #get string of text content of pdf

            text_filename = txtDir + pdf + ".txt"
            text_file = open(text_filename, "w", encoding = "utf-8")
            text_file.write(text)
            
            text_file.close()

# set paths accordingly:
pdfDir = "../data/"
txtDir = "./scripts/output/"
convertMultiple(pdfDir, txtDir)
