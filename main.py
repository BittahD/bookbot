def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    print(f"This book has {words} words and ")
    
def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def get_word_count(book):
    words = book.split()
    return len(words)
main()