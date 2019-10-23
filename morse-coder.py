import json


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
        try:
            if letter in dictionary.keys():
                value = '{} '.format(dictionary[letter])
                new_array.append(value)
        except:
            new_array.append('{}: {} '.format("Character not found", letter))
    new_string = ''.join(new_array)
    return new_string


def main():
    while True:
        morse_data = load_dict()
        if morse_data == None:
            return None

        user_input = input('Enter Message: ')

        new_string = to_morse_code(user_input, morse_data)

        print(new_string)


if __name__ == "__main__":
    main()
