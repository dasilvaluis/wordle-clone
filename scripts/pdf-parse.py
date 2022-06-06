import os

from helpers.text import (
    clean_duplicates,
    clean_joint_letters,
    clean_line_breaks,
    clean_ordinal_o,
    clean_punctuation,
    filter_by_element_len_of,
    filter_foreign_words,
    join_broken_words,
    filter_numbers,
    filter_words_with_minus,
    text_to_list,
    words_to_lowercase
)

from helpers.functional import (
    composite,
    tap_print,
)

from helpers.files import convert_pdf_to_text, find_pdf_files, save_output_to_json
from scripts.helpers.utils import find_duplicated_words

NEEDED_WORD_LENGTH = 5

cleanup_words_list = composite(
    clean_duplicates,
    tap_print("- cleaning duplicates"),
    filter_foreign_words,
    tap_print("- filtering foreign words"),
    words_to_lowercase,
    tap_print("- transforming words to lowercase"),
    filter_by_element_len_of(NEEDED_WORD_LENGTH),
    tap_print("- filtering words with len != " + str(NEEDED_WORD_LENGTH)),
    filter_words_with_minus,
    tap_print("- filtering minus"),
    filter_numbers,
    tap_print("- filtering numbers")
)

pdf_to_word_list = composite(
    text_to_list,
    tap_print("- converting text to list"),
    clean_ordinal_o,
    tap_print("- cleaning ordinal symbol"),
    clean_joint_letters,
    tap_print("- cleaning joint letters"),
    clean_punctuation,
    tap_print("- cleaning punctuation"),
    clean_line_breaks,
    tap_print("- cleaning line breaks"),
    join_broken_words,
    tap_print("- joining broken words"),
    convert_pdf_to_text,
    tap_print("- converting pdf to text"),
)

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convert_multiple_pdf_to_text(pdf_dir, out_dir):
    if type(out_dir) != str or out_dir == "" : out_dir = os.getcwd() + "/" 

    out_file = out_dir + "words.json"

    all_words = []

    pdf_files = find_pdf_files(pdf_dir)

    for filename in pdf_files:
        print("Found file: " + filename)

        source_pdf_filename = pdf_dir + filename

        words_from_pdf = pdf_to_word_list(source_pdf_filename)
        cleaned_words = cleanup_words_list(words_from_pdf)

        all_words.extend(cleaned_words)

    if (len(all_words) > 0): 
        print("Finished parsing files. Collecting duplicates..")

        filtered_words = find_duplicated_words(all_words)

        print("Finished processing text. Saving list to file: " + out_file)

        save_output_to_json(out_file, filtered_words)
    else:
        print("No words.")

# set paths:
script_dir = os.path.dirname(__file__)
pdfDir = os.path.join(script_dir, "../data/")
outDir = os.path.join(script_dir, "../words-dataset/")

convert_multiple_pdf_to_text(pdfDir, outDir)

