""" Works with text!!! """
import string


def get_words_data(text: str):
    """_summary_

    Args:
        text (str): _description_

    Returns:
        _type_: _description_
    """
    all_words = text.split(" ")
    words = []
    words_amount = []
    words_and_amount = {}
    for word in all_words:
        if word not in words:
            words.append(word)
            amount = text.count(word)
            words_and_amount[word] = amount
            words_amount.append(amount)

    return {"words": words, "words_amount": words_amount, "words_and_amount": words_and_amount}


def get_words_with(text: str, letter: str, position=None):
    """ Gets all words with string in a specific position.

    Args:
        text (str): The text
        letter (str): The string to search
        position (_type_, optional): The specific position. Defaults to None.

    Returns:
        _type_: str[]
    """
    words = text.split(" ")
    words_with_letter = []
    for word in words:
        if letter.index(position) == word:
            words_with_letter.append(word)
    return words_with_letter


def get_words_start_upper(text: str):
    """Gets all words that starts upper case letter.

    Args:
        text (str): _description_

    Returns:
        _type_: _description_
    """
    words = text.split(" ")
    words_start_upper = []
    for word in words:
        if word.index(0).isupper():
            words_start_upper.append(word)
    return words_start_upper


def read_file(path: str):
    with open(path, 'r', encoding='utf-8') as datafile:
        file_lines = datafile.readlines()
        file_content = "".join(file_lines)
        for line in file_lines:
            if "amor" in line.lower():
                print(line)


def caesar(plain_text: str, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)

    return plain_text.translate(trantab)


def encrypt_to_caesar(text: str, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    tran_table = str.maketrans(letters, mask)
    return text.translate(tran_table)


def decrypt_from_caesar(text: str, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    tran_table = str.maketrans(mask, letters)
    return text.translate(tran_table)


setence = encrypt_to_caesar("diogo neves neves", 4)
print("\n")
print(setence)
print(decrypt_from_caesar(setence, 4))
