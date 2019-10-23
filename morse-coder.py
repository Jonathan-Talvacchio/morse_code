import json
import os
from sys import platform


def clear_term():
    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def load_dict():
    try:
        with open('morse-code.json') as json_file:
            data = json.load(json_file)
    except:
        print('morse-code dictionary not loaded correctly!')
        return None
    else:
        return data


def to_morse_code(input_array, dictionary):
    new_array = []
    for letter in input_array:
        if letter in dictionary.keys():
            value = '{} '.format(dictionary[letter])
            new_array.append(value)
        else:
            new_array.append('{}: {} '.format("Character not found", letter))
    new_string = ''.join(new_array)
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
        if morse_dictionary == None:
            return None

        # create reverse dictionary
        r_dictionary = reverse_dictionary(morse_dictionary)

        prompt_message = 'Enter Message: ' if to_morse else 'Enter Code: '
        user_input = input(prompt_message)
        user_input = user_input.lower()

        if user_input == '/t':
            to_morse = not to_morse
            continue
        if user_input == '/c':
            clear_term()
            continue

        if to_morse:
            new_string = to_morse_code(user_input, morse_dictionary)
        else:
            user_input = user_input.split()
            new_string = to_morse_code(user_input, r_dictionary)

        print(new_string)


if __name__ == "__main__":
    main()
