"""
Book analyzer util functions
"""


def get_word_count(text: str) -> int:
    return len(text.split())


def get_letter_count(text: str) -> dict[str, int]:
    appearances = {}
    words = text.split()
    for w in words:
        w = w.lower()
        for ch in w:
            if not ch.isalpha():
                continue
            if ch in appearances:
                appearances[ch] += 1
            else:
                appearances[ch] = 1
    return appearances


def print_char_count(count: dict[str, int]) -> None:
    sorted_count = dict(
        sorted(count.items(), key=lambda x: x[1], reverse=True))

    for k, v in sorted_count.items():
        print(f"The '{k}' character was found {v} times")
