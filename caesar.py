import string


def caesar(plain_text: str, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)

    return plain_text.translate(trantab)


print(caesar("diogo neves", 4))


def shift_n2(letter, amount):
    if letter not in string.ascii_lowercase:
        return letter
    new_letter = ord(letter) + amount
    while new_letter > ord('z'):
        new_letter -= 26
    while new_letter < ord("a"):
        new_letter += 26

    return chr(new_letter)


def caesar2(message, amount):
    enc_list = [shift_n2(letter, amount) for letter in message]
    return "".join(enc_list)


def shift_n3(letter, table):
    try:
        index = string.ascii_lowercase.index(letter)
        return table[index]
    except ValueError:
        return letter


def caesar3(message, amount):
    amount = amount % 26
    ascii_lowercase = string.ascii_lowercase
    table = ascii_lowercase[amount:] + ascii_lowercase[:amount]
    enc_list = [shift_n3(letter, table) for letter in message]

    return "".join(enc_list)
