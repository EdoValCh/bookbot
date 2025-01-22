def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    list_of_dictionaries = []
    for i in character_count:
        if i.isalpha():
            list_of_dictionaries += [
                {"name" : i, "num": character_count[i]}
            ]
    list_of_dictionaries.sort(reverse=True,key=sort_on)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{num_words} words found in the document')
    print('')   
    for i in list_of_dictionaries:
        print(f"The '{i["name"]}' character was found {i["num"]} times")
    print('--- End report ---')


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    words_dict = {}
    for character in text.lower():
        if character in words_dict:
            words_dict[character] += 1
        else:
            words_dict[character] = 1
    return words_dict

def sort_on(dict):
    return dict["num"]

main()