import unittest
from unittest.mock import patch

from editor import MarkdownEditor


class TestEditor(unittest.TestCase):
    urs_inp = [3, 'This is header',
               3, 'This is header',
               10]

    @patch('builtins.input', side_effect=urs_inp)
    def test_heading(self, mock_input):
        mrkd_editor = MarkdownEditor()
        self.assertEqual(mrkd_editor.heading(''), '### This is header\n')
        self.assertEqual(mrkd_editor.heading('foobar'), '\n### This is header\n')

    @patch('builtins.input', return_value='Bold text')
    def test_bold_text(self, mock_input):
        mrkd_editor = MarkdownEditor()
        self.assertEqual(mrkd_editor.bold(), '**Bold text**')

    @patch('builtins.input', return_value='Italic text')
    def test_italic_text(self, mock_input):
        mrkd_editor = MarkdownEditor()
        self.assertEqual(mrkd_editor.italic(), '*Italic text*')

    @patch('builtins.input', return_value='plain text')
    def test_plain_text(self, mock_input):
        mrkd_editor = MarkdownEditor()
        self.assertEqual(mrkd_editor.plain_text(), 'plain text')

    @patch('builtins.input', return_value='inline code')
    def test_inline_code(self, mock_input):
        mrkd_editor = MarkdownEditor()
        self.assertEqual(mrkd_editor.inline_code(), '`inline code`')

    def test_new_line(self):
        mrkd_editor = MarkdownEditor()
        self.assertEqual(mrkd_editor.new_line(), '\n')
        self.assertNotEqual(mrkd_editor.new_line(), 'foobar')

    @patch('builtins.input', side_effect=['Google link', 'www.google.com'])
    def test_link(self, mock_input):
        mrkd_editor = MarkdownEditor()
        self.assertEqual(mrkd_editor.link(), '[Google link](www.google.com)')

    lists = ['3', 'first row', 'second row', 'third row',
             '3', 'first row', 'second row', 'third row', ]

    @patch('builtins.input', side_effect=lists)
    def test_lists(self, mock_input):
        mrkd_editor = MarkdownEditor()
        self.assertEqual(mrkd_editor.lists('ordered-list'),
                         '1. first row\n2. second row\n3. third row\n')
        self.assertEqual(mrkd_editor.lists('unordered-list'),
                         '* first row\n* second row\n* third row\n')





















