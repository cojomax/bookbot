def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    dictionary = {}
    for c in text:
        _c = c.lower()
        if _c not in dictionary:
            dictionary[_c] = 0
        dictionary[_c] += 1
    return dictionary