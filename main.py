from stats import count_chars, count_words, get_book_text

def main():
    contents = get_book_text("books/frankenstein.txt")
    # print(f"Found {count_words(contents)} total words")
    print(count_chars(contents))
    
main()
