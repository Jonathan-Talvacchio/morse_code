import json
import os
from sys import platform


def clear_term():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def load_dict():
    try:
        DICTIONARY_NAME = "morse_code.json"

        # get script file for dictionary
        current_file = __file__
        real_path = os.path.realpath(current_file)
        dir_path = os.path.dirname(real_path)
        dictionary_file = "{}/{}".format(dir_path, DICTIONARY_NAME)

        with open(dictionary_file) as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(f"morse_code.json dictionary not loaded correctly!\n"
              f"{e}")
        return None
    else:
        return data


def translator(input_array, dictionary):
    new_array = []
    for letter in input_array:
        if letter in dictionary.keys():
            value = f"{dictionary[letter]} "
            new_array.append(value)
        else:
            new_array.append("{}: {} ".format("CHAR not found", letter))
    new_string = "".join(new_array)
    return new_string


def reverse_dictionary(dictionary):
    r_dictionary = {}
    for i in dictionary:
        r_dictionary[dictionary[i]] = i
    return r_dictionary


def main():
    clear_term()
    to_morse = True
    while True:
        # load morse code dictionary
        morse_dictionary = load_dict()
        if morse_dictionary is None:
            quit()

        # create reverse dictionary
        r_dictionary = reverse_dictionary(morse_dictionary)

        message_prompt = "Enter Message: " if to_morse else "Enter Code: "
        usr_input = input(message_prompt)
        usr_input = usr_input.lower()

        if usr_input == "/t":
            to_morse = not to_morse
            continue
        if usr_input == "/c":
            clear_term()
            continue
        if usr_input == "/q":
            quit()

        # Translate to mores code
        if to_morse:
            return_string = translator(usr_input, morse_dictionary)
        # Translate to English
        else:
            usr_input = usr_input.split()
            return_string = translator(usr_input, r_dictionary)

        print(return_string)


if __name__ == "__main__":
    main()
