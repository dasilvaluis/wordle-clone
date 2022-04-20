import io
import os
import json
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from helpers import (
    clean_duplicates,
    clean_line_breaks,
    clean_punctuation,
    composite,
    filter_by_element_len_of,
    text_to_list,
    words_to_lowercase
)

NEEDED_WORD_LENGTH = 4

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

def save_output_to_json(filename, li):
    data = {
        "data": li
    }

    with open(filename, "w", encoding = "utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


build_four_letter_words_list = composite(
    clean_duplicates,
    words_to_lowercase,
    filter_by_element_len_of(NEEDED_WORD_LENGTH),
    text_to_list,
    clean_punctuation,
    clean_line_breaks,
    convert_pdf_to_text
)

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, outDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 

    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        file_extension = pdf.split(".")[-1]

        if file_extension == "pdf":
            source_pdf_filename = pdfDir + pdf 
            output_filename = outDir + pdf + ".json"
            
            four_letter_words = build_four_letter_words_list(source_pdf_filename)

            save_output_to_json(output_filename, four_letter_words)


script_dir = os.path.dirname(__file__)

# set paths accordingly:
pdfDir = os.path.join(script_dir, "..\data\\")
outDir = os.path.join(script_dir, "output\\")

convertMultiple(pdfDir, outDir)

