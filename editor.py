# write your code here

FORMATTING_LST = ['plain', 'bold', 'italic', 'header', 'link',
                  'inline-code', 'unordered-list',  'ordered-list', 'new-line']


def available_formatters():
    formatter = """Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done"""

    return formatter


def main():

    while True:
        usr_inp = input('Chose a formatter: ')

        if usr_inp == '!done':
            break

        if usr_inp == '!help':
            print(available_formatters())

        if usr_inp not in FORMATTING_LST and usr_inp not in ['!help', '!done']:
            print('Unknown formatting type or command')


if __name__ == '__main__':
    main()
