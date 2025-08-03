"""
CP1404/CP5632 Practical
Testing using assertions and doctests
"""

import doctest
from prac_06.car import Car


def repeat_text(text, times):
    """Return the text repeated `times` with spaces in between."""
    return " ".join([text] * times)


def check_word_length(word, min_length=5):
    """
    Return True if word length is greater than or equal to min_length.
    >>> check_word_length("not")
    False
    >>> check_word_length("supercalifrag")
    True
    >>> check_word_length("Python", 6)
    True
    """
    return len(word) >= min_length


def make_sentence(phrase):
    """
    Capitalize the first letter of phrase and ensure it ends with a period.
    >>> make_sentence('hello')
    'Hello.'
    >>> make_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> make_sentence('this needs formatting')
    'This needs formatting.'
    """
    phrase = phrase.capitalize()
    return phrase if phrase.endswith('.') else phrase + '.'



