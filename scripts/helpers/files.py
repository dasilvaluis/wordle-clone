import json
import os
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def is_pdf_file(x) :
  return x.split(".")[-1] == "pdf"
  
  
def find_pdf_files(pdf_dir):
    if type(pdf_dir) != str or pdf_dir == "" : pdf_dir = os.getcwd() + "/" 

    pdf_files = filter(is_pdf_file, os.listdir(pdf_dir))

    return pdf_files

def save_output_to_json(filename, data):
    data = {
        "data": data
    }

    with open(filename, "w", encoding = "utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#converts pdf, returns its text content as a string
def convert_pdf_to_text(fname, pages = None):
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
