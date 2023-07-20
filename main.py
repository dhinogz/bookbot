"""
Bookbot - A simple book analyzer program.
Exercise found at: https://boot.dev/learn/build-local-dev-environment-python
"""

import os
import util

DIR = "books/"


def main():
    for file_name in os.listdir(DIR):
        file = f"{DIR}{file_name}"
        run_report(file)


def run_report(file: str) -> None:
    with open(file) as f:
        text = f.read()

    print(f"\n--- Begin report of {file} ---\n")

    words = util.get_word_count(text)
    print(f"{words} words found in the document\n")

    char_count = util.get_letter_count(text)
    util.print_char_count(char_count)

    print("\n--- End report ---\n")


if __name__ == "__main__":
    main()
