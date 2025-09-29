from stats import get_num_words
from stats import count_characters
from stats import sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    num_characters = count_characters(book_text, {})
    sorted_characters = sort_char_dict(num_characters)
    
    print("================BOOKBOT===================")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------------Word Count------------------")
    print(f"Found {num_words} total words")
    print("---------------Character Count--------------")
    for char, count in sorted_characters:
        print(f"{char}: {count}")
    print("==================END=====================")
    

if __name__ == "__main__":
    main()
