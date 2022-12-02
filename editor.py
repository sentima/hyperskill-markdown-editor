def main():
    formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
    text = ''

    while True:
        input_formatter = input('Choose a formatter: ')
        if input_formatter == '!help':
            help_f()
        elif input_formatter in formatters:
            if input_formatter == formatters[0]:
                text += plain()
            elif input_formatter == formatters[1]:
                text += bold()
            elif input_formatter == formatters[2]:
                text += italic()
            elif input_formatter == formatters[3]:
                text += header()
            elif input_formatter == formatters[4]:
                text += link()
            elif input_formatter == formatters[5]:
                text += inline_code()
            elif input_formatter == formatters[6]:
                text += add_list(1)
            elif input_formatter == formatters[7]:
                text += add_list()
            elif input_formatter == formatters[8]:
                text += new_line()

            print(text)

        elif input_formatter == '!done':
            file = open('output.md', 'w', encoding='utf-8')
            file.write(text)
            file.close()
            break
        else:
            print('Unknown formatting type or command')


def help_f():
    print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n'
          'Special commands: !help !done')


def ask_text():
    text = input('Text: ')
    return text


def add_list(order=None):
    while True:
        rows = int(input('Number of rows: '))
        if rows <= 0:
            print('The number of rows should be greater than zero')
        else:
            break

    elements = ''
    for row in range(1, rows + 1):
        if order is None:
            elements += f'# {input(f"Row #{row}: ")}\n'
        else:
            elements += f'{row}. {input(f"Row #{row}: ")}\n'
    return elements


def new_line():
    return '\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def header():
    while True:
        level = int(input('Level: '))
        if level in range(1, 7):
            break
        else:
            print('The level should be within the range of 1 to 6')

    return level * '#' + f' {ask_text()}\n'


def bold():
    return f'**{ask_text()}**'


def inline_code():
    return f'`{ask_text()}`'


def italic():
    return f'*{ask_text()}*'


def plain():
    return ask_text()


if __name__ == "__main__":
    main()
