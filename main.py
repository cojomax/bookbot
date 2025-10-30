import sys
from stats import create_char_count, count_words, create_report_data, get_book_text

def print_report(book_path, word_count, data):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in data:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    sorted_data = create_report_data(create_char_count(content))

    print_report(book_path, count_words(content), sorted_data)

main()
