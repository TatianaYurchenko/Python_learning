# def reverse_string_slicing(s):
#     return s[::-1]
#
# print(reverse_string_slicing('With platform'))
from curses.ascii import isalnum


def is_palindrome(text):
    clean_text = ''.join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]
