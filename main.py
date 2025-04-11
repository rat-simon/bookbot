from stats import get_book_text, get_words, get_letters, sort_letters
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_words(text)
    letter_dict = get_letters(text)
    sorted_letters = sort_letters(letter_dict)
    print(f"Found {word_count} total words")


    # print header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    # print word count

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Print the character count section
    print("--------- Character Count -------")

    #print letter and count

    for item in sorted_letters:
        character = item["letter"]
        count = item["count"]
        #only print in alphabetical order

        if character.isalpha():
            print(f"{character}: {count}")
    #footer
    print("============= END ===============")
main()

