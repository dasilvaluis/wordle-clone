import json
import os

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
