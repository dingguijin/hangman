import unittest

from hangman import guess_next_letter

def test_function_should_return_something():
    pattern = "____e"
    used_letters = list("abcde")
    word_list = [...]
    assert guess_next_letter(pattern, used_letters, word_list) is not None

def test_function_already_matched_in_pattern():
    pattern = "a____t"
    used_letters = list("wy")
    word_list = ["alphabet"]
    assert guess_next_letter(pattern, used_letters, word_list) is not None

if __name__ == "__main__":
    test_function_should_return_something()
    test_function_already_matched_in_pattern()
