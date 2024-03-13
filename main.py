def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars = char_frequency(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char_dict in sort_char_count(chars):
        print(f"The {char_dict['char']} character was found {char_dict['freq']} times")
    print("--- End report ---")
        

def char_frequency(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            lowercase_char = char.lower()
            if lowercase_char not in char_dict:
                char_dict[lowercase_char] = 1
            else:
                char_dict[lowercase_char] += 1
    return char_dict

def get_book_text(path):
     with open(path) as f:
         return f.read()

def count_words(text):
    words = len(text.split())
    return words

def sort_char_count(char_dict):
    def sort_on(dict_item):
        return dict_item["freq"]

    list_of_dict = []
    for key in char_dict:
        list_of_dict.append({"char": key, "freq": char_dict[key]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

main()
