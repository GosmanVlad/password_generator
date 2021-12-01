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

def string_to_list(string):
    final_list = []
    for i in range(0, len(string)):
        final_list.append(string[i])
    return final_list


def generate_random_password():
    final_password = ""

    random_length = random.randint(min_chars, max_chars)
    random_symbols = symbols[random.randint(0, 3)]
    first_char = ''.join(random.choices(upper, k=1))

    final_password += first_char


def merge_lists(lower, upper, numbers, symbols):
    return lower + upper + numbers + symbols


if __name__ == "__main__":
    lower_list = string_to_list(lower)
    upper_list = string_to_list(upper)
    numbers_list = string_to_list(numbers)
    symbols_list = string_to_list(symbols)

    test = merge_lists(lower_list, upper_list, numbers_list, symbols_list)
    print(shuffle(test, random_state=3))

    if len(sys.argv) > 0:
        if len(sys.argv) > 1:
            if sys.argv[1] == '-use-dict':
                print("Get data from file")
        else:
            generate_random_password()