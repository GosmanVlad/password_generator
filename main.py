import string
import random
import sys
import numpy
from sklearn.utils import shuffle

max_chars = 18
min_chars = 12

#string:
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = "!?#@"

#lists:
lower_list = []
upper_list = []
numbers_list = []
symbols_list = []
words_list = []

def read_words():
    with open("dictionary.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def string_to_list(string):
    final_list = []
    for i in range(0, len(string)):
        final_list.append(string[i])
    return final_list


def check_if_string_contains_symbols(password):
    for symbol in symbols_list:
        if symbol in password:
            return True
    return False


def generate_random_password(type, list):
    final_password = ""

    if type == "auto":
        random_length = random.randint(min_chars, max_chars)
        random_symbols = symbols[random.randint(0, 3)]
        first_char = ''.join(random.choices(upper, k=1))

        final_password += first_char
        for i in range(0, random_length-1):
            final_password += list[i]

        if not check_if_string_contains_symbols(final_password):
            final_password = final_password.replace(final_password[random.randint(0, len(final_password)-1)], random_symbols)

    if type == "dictionary":
        words_list = read_words()
        words_list = shuffle(words_list, random_state=3)
        random_length = random.randint(min_chars, max_chars)
        random_symbols = symbols[random.randint(0, 3)]

        index = 0
        for word in words_list:
            random_symbols = symbols[random.randint(0, 3)]
            if len(final_password + word) < random_length:
                if random.randint(0, 100) % 2 == 0 and index != 0:
                    final_password += random_symbols
                else:
                    final_password += word
            index += 1


        for i in range(0, random_length - len(final_password)):
            random_symbols = symbols[random.randint(0, 3)]
            if len(final_password) < random_length:
                if not check_if_string_contains_symbols(final_password):
                    final_password += random_symbols
                else:
                    final_password += list[i]

    return final_password




def merge_lists(lower, upper, numbers, symbols):
    return lower + upper + numbers + symbols


if __name__ == "__main__":
    final_password = ""
    generate_type = ""

    lower_list = string_to_list(lower)
    upper_list = string_to_list(upper)
    numbers_list = string_to_list(numbers)
    symbols_list = string_to_list(symbols)
    entire_list = merge_lists(lower_list, upper_list, numbers_list, symbols_list)
    entire_list = shuffle(entire_list, random_state=random.randint(0, 100))
    
    if len(sys.argv) > 0:
        if len(sys.argv) > 1:
            if sys.argv[1] == '-use_dict':
                final_password = generate_random_password("dictionary", entire_list)
                generate_type = "dictionary"
        else:
            final_password = generate_random_password("auto", entire_list)
            generate_type = "auto"

    print("Parola generata: " + final_password)
    print("Marime parola: " + str(len(final_password)))
    print("Tip generare: " + generate_type)