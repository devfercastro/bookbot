from collections import Counter
from typing import Dict


def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    book_content_word_count = get_word_count(book_content)
    character_count = count_characters(book_content)
    # print(book_content)
    print(book_content_word_count)
    print(character_count)
    print_characters_report(character_count, book_content_word_count, book_path)


def get_book_content(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_word_count(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> Dict[str, int]:
    return Counter(text.lower())


def print_characters_report(data: Dict[str, int], words_count: int, book_path: str):
    sorted_data = sorted(list(data.items()), key=lambda tp: tp[0])

    print(f"-- Begin report of {book_path}")
    print(f"{words_count} words found in the document\n")

    for char, count in sorted_data:
        print(f"The '{char}' character was found {count} times")


main()
