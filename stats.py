def get_book_txt(file_path):
    with open(file_path) as f:
        return f.read()
    
def get_num_words(text):
    return len(text.split())


def get_word_count_by_letter(text):
    word_count_by_letter = {}
    for word in text.split():
        for letter in word:
            if letter.isalpha():
                word_count_by_letter[letter.lower()] = word_count_by_letter.get(letter.lower(), 0) + 1
    return word_count_by_letter

def sort_word_count_by_letter(word_count_dictionary):
    return sorted(word_count_dictionary.items(), key=lambda x: x[1], reverse=True)