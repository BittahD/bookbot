import re

def main():
    #path to the book
    book_path = "books/frankenstein.txt"
    #read .txt file into CLI
    text = get_book_text(book_path)
    #word count within a .txt file        
    words = get_word_count(text)
    #dict with individual letter count
    letters = {}
    get_letter_count(text, letters)
    print(f"This book has {words} words and {letters} ")
    
def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def get_word_count(book):
    words = book.split()
    return len(words)

def get_letter_count(text, letter_dict):
    for index, letter in enumerate(text):
        if letter not re.match([A-Za-z]):
            continue
        if letter not in letter_dict:
           letter_dict.setdefault(letter.lower(), 1)
        if letter in letter_dict:
            letter_dict[letter] += 1

main()
