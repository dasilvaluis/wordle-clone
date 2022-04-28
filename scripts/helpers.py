from typing import List
from functools import reduce

def text_to_list(text: str):
    return list(text.split(" "))

def clean_punctuation(text: str):
    punc = '''!()„…’[]{};:'"\,<>./?@#$%^&*_~'''
    
    for ele in text:
        if ele in punc:
            text = text.replace(ele, "")

    return text

def replace_text_with_pairs(pairs, text):
    def replace_text(acc, pair):
        return acc.replace(pair[0], pair[1])

    return reduce(replace_text, pairs, text)

def clean_joint_letters(text: str):
    pairs = [
        ("ﬂ", "fl"),
        ("ﬁ", "fi")
    ]

    return replace_text_with_pairs(pairs, text)

def join_broken_words(text: str):
    pairs = [
        ("-\n", "")
    ]

    return replace_text_with_pairs(pairs, text)

def clean_line_breaks(text: str):
    pairs = [
        ("\n", " "),
        ("\f", " ")
    ]

    return replace_text_with_pairs(pairs, text)

def clean_duplicates(wordsList: List[str]):
    return list(dict.fromkeys(wordsList))

def filter_by_element_len_of(length: int):
    return lambda li : [word for word in li if len(word) == length]

def words_to_lowercase(wordsList: List[str]):
    return map(lambda x : x.lower(), wordsList)

def filter_words_with_minus(wordsList: List[str]):
    without_minus = lambda x : '-' not in x

    return filter(without_minus, wordsList)

def filter_foreign_words(wordsList: List[str]):
    foreign_letters = 'kwyç'
    probably_not_foreign = lambda w : not any(l in w for l in foreign_letters)

    return filter(probably_not_foreign, wordsList)

def filter_numbers(wordsList: List[str]):
    without_numbers = lambda s : not any(i.isdigit() for i in s)

    return filter(without_numbers, wordsList)
