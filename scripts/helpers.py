from functools import reduce

def composite(*func):
    def compose(f, g):
        return lambda x : f(g(x))
    
    return reduce(compose, func, lambda x : x)

def text_to_list(text):
    return list(text.split(" "))

def clean_punctuation(text):
    punc = '''!()„[]{};:'"\,<>./?@#$%^&*_~'''

    for ele in text:
        if ele in punc:
            text = text.replace(ele, "")

    return text

def clean_line_breaks(text):
    return text.replace("\n", " ").replace("\f", " ")

def clean_duplicates(wordsList):
    return list(dict.fromkeys(wordsList))

def filter_by_element_len_of(length):
    return lambda li : [word for word in li if len(word) == length]

def words_to_lowercase(wordsList):
    return map(lambda x : x.lower(), wordsList)
