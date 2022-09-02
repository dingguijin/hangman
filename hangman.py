import random
import string

def guess_next_letter(pattern, used_letters=[], word_list=["about", "abound", ...]):
    letter_freq = {}
    for word in word_list:
        if isinstance(word, type(...)):
            continue
        for letter in word:
            if len(word) != len(pattern):
                continue
            if letter in used_letters:
                continue
            if letter in pattern:
                continue
            if letter not in letter_freq:
                letter_freq[letter] = 1
            else:
                letter_freq[letter] = letter_freq[letter] + 1
    if letter_freq:
        ret_letter = random.choices(list(letter_freq.keys()), weights=list(letter_freq.values()))[0]
        print(ret_letter)
        return ret_letter
    
    # if not letter_freq:
    letters = list(string.ascii_lowercase)
    for letter in used_letters:
        if letter in letters:
            letters.remove(letter)
    for letter in pattern:
        if letter != "_" and letter in letters:
            letters.remove(letter)
    ret_letter = random.choice(letters)
    print(ret_letter)
    return ret_letter

