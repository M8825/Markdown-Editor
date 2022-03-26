# write your code here
# 'unordered-list',  'ordered-list',
class MarkdownEditor:
    FORMATTING_LST = ['plain', 'bold', 'italic', 'header',
                      'link', 'inline-code', 'new-line']

    formatter = "Available formatters: plain bold italic header link inline-code new-line"
    special = "Special commands: !help !done"

    def heading(self, text_line):
        while True:
            level = int(input('Level: '))
            if not 0 < level < 6:
                print("The level should be within the range of 1 to 6")
                continue
            heading_text = input('Text: ')

            level = '#' * level
            if text_line:
                return f'\n{level} {heading_text}\n'
            return f'{level} {heading_text}\n'

    def bold(self):
        bold_text = input('Text: ')
        return f'**{bold_text}**'

    def italic(self):
        italic_text = input('Text: ')
        return f'*{italic_text}*'

    def plain_text(self):
        plain_text = input('Text: ')
        return plain_text

    def inline_code(self):
        inline_code = input('Text: ')
        return f'`{inline_code}`'

    def new_line(self):
        return f'\n'

    def link(self):
        label = input('Label: ')
        url = input('URL: ')
        return f'[{label}]({url})'

    def main(self):
        text = ''

        while True:
            if text != '':
                print(text)
            usr_inp = input('Chose a formatter: ')

            if usr_inp not in self.FORMATTING_LST and usr_inp not in ['!help', '!done']:
                print('Unknown formatting type or command')

            if usr_inp == '!done':
                break

            if usr_inp == '!help':
                print(self.formatter)
                print(self.special)
            if usr_inp == 'header':
                text += self.heading(text)
            elif usr_inp == 'plain':
                text += self.plain_text()
            elif usr_inp == 'inline-code':
                text += self.inline_code()
            elif usr_inp == 'new-line':
                text += self.new_line()
            elif usr_inp == 'bold':
                text += self.bold()
            elif usr_inp == 'link':
                text += self.link()
            elif usr_inp == 'italic':
                text += self.italic()


if __name__ == '__main__':
    MarkdownEditor().main()
