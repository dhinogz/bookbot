"""
Bookbot - A simple book analyzer program.
Exercise found at: https://boot.dev/learn/build-local-dev-environment-python
"""

import util

FILE = "books/frankenstein.txt"


def main():
    with open(FILE) as f:
        text = f.read()

    print(f"--- Begin report of {FILE} ---")

    words = util.get_word_count(text)
    print(f"{words} words found in the document\n")

    char_count = util.get_letter_count(text)
    util.print_char_count(char_count)

    print("--- End report --- ")


if __name__ == "__main__":
    main()
