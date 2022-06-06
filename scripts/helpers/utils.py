
def find_duplicated_words(words: list[str]):
    seen = set()
    dupes = []

    for w in words:
        if w in seen:
            dupes.append(w)
        else:
            seen.add(w)
     
    return dupes