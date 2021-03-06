import string
import random
import sys
# from sklearn.utils import shuffle
from sklearn.utils import shuffle

max_chars = 18
min_chars = 12

# string:
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = "!?#@"


# Functie care citeste din fisierul dictionary.txt, linie cu linie
# si returneaza o lista cu toate cuvintele citite
def read_words():
    with open("dictionary.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


# Functie care verifica daca intr-un string sunt simboluri
# Params: password - string-ul in care vom verifica aparitia simbolurilor
def check_if_string_contains_symbols(password):
    symbols_list = list(symbols)
    for symbol in symbols_list:
        if symbol in password:
            return True
    return False


def generate_random_password(type, list):
    final_password = ""

    if type == "auto":
        # Alegem o lungime random cuprinsa intre min_chars si max_chars,
        # un simbol random si un caracter majuscula random pentru primul
        # char din parola
        random_length = random.randint(min_chars, max_chars)
        random_symbols = symbols[random.randint(0, 3)]
        first_char = ''.join(random.choices(upper, k=1))

        final_password += first_char
        for i in range(0, random_length - 1):
            final_password += list[i]

        # Daca parola obtinuta nu contine niciun simbol, atunci alegem o pozitie random
        # din parola formata pana acum si inlocuim char-ul ales cu un symbol random
        if not check_if_string_contains_symbols(final_password):
            final_password = final_password.replace(final_password[random.randint(0, len(final_password) - 1)],
                                                    random_symbols)

    if type == "dictionary":
        # Citim din fisier fiecare cuvant, il transformam intr-un string si il amestecam
        # Alegem o lungime random cuprinsa intre min_chars si max_chars
        words_list = read_words()
        words_list = shuffle(words_list, random_state=random.randint(0, 100))
        random_length = random.randint(min_chars, max_chars)

        index = 0

        # Parcurgem lista de cuvinte citite si verificam daca cuvantul de pe pozitia actuala
        # incepe cu o majuscula, in caz contrar se verifica urmatorul cuvant
        for word in words_list:
            random_symbols = symbols[random.randint(0, 3)]
            isUpper = False
            if index == 0:
                isUpper = True

            if len(final_password + word) < random_length:
                # Avand in vedere ca in lista de cuvinte nu se regaseste niciun simbol,
                # alegem aleator prin aceasta conditie sa introducem un simbol, sau nu
                if random.randint(0, 100) % 2 == 0 and index != 0:
                    final_password += random_symbols
                else:
                    if isUpper:
                        if word[0].isupper():
                            final_password += word
                            index += 1
                    else:
                        final_password += word
                        index += 1

        # Daca combinatia dintre cuvinte formata in for-ul nu respecta lungimea aleasa
        # se completeaza atat cu simboluri cat si cu caractere alfanumerice
        for i in range(0, random_length - len(final_password)):
            random_symbols = symbols[random.randint(0, 3)]
            if len(final_password) < random_length:
                if not check_if_string_contains_symbols(final_password):
                    final_password += random_symbols
                else:
                    final_password += list[i]

    return final_password


if __name__ == "__main__":
    final_password = ""
    generate_type = ""

    # Convertim toate caracterele intr-o singura lista si le amestecam random
    # pentru a obtine parola finala, respectand conditiile impuse in cerinta
    entire_list = list(lower + upper + numbers + symbols)
    entire_list = shuffle(entire_list, random_state=random.randint(0, 100))

    # In functie de argumentul dat la rulare, algoritmul va genera parola finala
    # tinand cont de conditiile impuse in cerinta
    # Pentru niciun argument dat, algoritmul va creea random o parola
    # folosindu-se de caracterele alfanumerice si de simboluri
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
    print(
        'Tip generare: generare automata' if generate_type == "auto" else 'Tip generare: generare utilizand dictionarul')
