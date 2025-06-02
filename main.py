from stats import get_book_txt, get_num_words, get_word_count_by_letter, sort_word_count_by_letter
import sys


def main():
    print("============ BOOKBOT ============")
    entries = sys.argv
    if len(entries) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print(f"Analyzing book found at {entries[1]}...")
    
    book_txt = get_book_txt(entries[1])
    print("----------- Word Count ----------")
    total_words = get_num_words(book_txt)
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    word_count_by_letter = get_word_count_by_letter(book_txt)
    sorted_word_count_by_letter = sort_word_count_by_letter(word_count_by_letter)
    for letter, count in sorted_word_count_by_letter:
        print(f"{letter}: {count}")
    print("============= END ===============")

main()

