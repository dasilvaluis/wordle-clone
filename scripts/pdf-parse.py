from ast import If
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
    filter_numbers,
    filter_words_with_minus,
    lambda_print,
    tap,
    text_to_list,
    words_to_lowercase
)

NEEDED_WORD_LENGTH = 5

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

tap_print = lambda t : tap(lambda_print(t))

cleanup_words_list = composite(
    clean_duplicates,
    tap_print("- 5/5 cleaning duplicates"),
    words_to_lowercase,
    tap_print("- 4/5 transforming words to lowercase"),
    filter_by_element_len_of(NEEDED_WORD_LENGTH),
    tap_print("- 3/5 filtering words with len != " + str(NEEDED_WORD_LENGTH)),
    filter_words_with_minus,
    tap_print("- 2/5 filtering minus"),
    filter_numbers,
    tap_print("- 1/5 filtering numbers")
)

pdf_to_word_list = composite(
    text_to_list,
    tap_print("- 4/4 converting text to list"),
    clean_punctuation,
    tap_print("- 3/4 cleaning punctuation"),
    clean_line_breaks,
    tap_print("- 2/4 cleaning line breaks"),
    convert_pdf_to_text,
    tap_print("- 1/4 converting pdf to text"),
)

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convert_multiple_pdf_to_text(pdf_dir, out_dir):
    if type(out_dir) != str or out_dir == "" : out_dir = os.getcwd() + "/" 
    if type(pdf_dir) != str or pdf_dir == "" : pdf_dir = os.getcwd() + "/" 

    out_file = out_dir + "output.json"

    all_words = []

    for pdf_file in os.listdir(pdf_dir):
        file_extension = pdf_file.split(".")[-1]

        if file_extension == "pdf":
            print("Found file: " + pdf_file)

            source_pdf_filename = pdf_dir + pdf_file

            words_from_pdf = pdf_to_word_list(source_pdf_filename)

            all_words.extend(words_from_pdf)


    if (len(all_words) > 0): 
        print("Finished parsing files. Processing text...")

        filtered_words = cleanup_words_list(all_words)

        print("Finished processing text. Saving list to file: " + out_file)

        save_output_to_json(out_file, filtered_words)
    else:
        print("No words.")

# set paths:
script_dir = os.path.dirname(__file__)
pdfDir = os.path.join(script_dir, "../data/")
outDir = os.path.join(script_dir, "./output/")

convert_multiple_pdf_to_text(pdfDir, outDir)

