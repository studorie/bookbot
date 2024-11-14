import re

path_to_file = "books/frankenstein.txt"
def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def split_words():
    total_words = 0
    read_book = main(path_to_file)
    test = read_book.split()
    for test in test:
        total_words += 1
    print(total_words)


def count_character():
    read_book = main(path_to_file)
    book_lower = read_book.lower()
    character_count = {}
    for character in book_lower:
        character_count[character] = character_count.get(character, 0) + 1
    return character_count



def print_report():
    report = count_character()
    for r in report.keys():
        print(f"The {r} character was found {report[r]} times")
