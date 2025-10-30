def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def create_char_count(text):
    dictionary = {}
    for c in text:
        _c = c.lower()
        if _c not in dictionary:
            dictionary[_c] = 0
        dictionary[_c] += 1
    return dictionary

def sort_on(items):
    return items["num"]

def create_report_data(dictionary):
    char_data = []
    for k in dictionary:
        char_data.append({ "char": k, "num": dictionary[k] })
    char_data.sort(reverse=True, key=sort_on)
    return char_data
