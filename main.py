def main():
    # path to the book
    file_path = "books/frankenstein.txt"
    # read .txt file into CLI
    text = get_file_text(file_path)
    # word count within a .txt file        
    words = get_word_count(text)
    # dict with individual letter count
    letter_dict = get_letter_count(text)
    # converting dict to list
    letter_list = dict_to_list(letter_dict)
    # call file_report
    file_report(file_path, words, letter_list)
    
def file_report(file, word_count, letter_list):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words were found in the document")
    print("\n")
    # sorting list
    sorted_list = sorted(letter_list, key=lambda letter_count: letter_count[1], reverse=True)
    # iterate through list and print results
    for l, n in sorted_list:
        print(f"The '{l}' character was found {n} times")
        
    print("--- End report ---")
    
def dict_to_list(dic):
    return dic.items()
    
def get_file_text(path):
    with open(path) as file:
        return file.read()
    
def get_word_count(file):
    words = file.split()
    return len(words)

def get_letter_count(text):
    letter_dict = {}
    for letter in text:
        low_letter = letter.lower()
        if low_letter not in letter_dict:
            if (low_letter.isalpha()) == True:
                letter_dict.setdefault(low_letter, 1)
        else:
            letter_dict[low_letter] += 1
    return letter_dict

main()
