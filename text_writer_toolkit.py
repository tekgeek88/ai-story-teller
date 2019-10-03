
def append_whitespace(word):
    temp_word = word[:]
    temp_word += ' '
    return temp_word

def append_new_line(word, new_line_char):
    temp_word = word[:]
    temp_word += new_line_char
    return temp_word

def append_newline_with_dash(word, index, new_line_char):
    temp_word = word[:index] + '-' + new_line_char + word[index:] + ' '
    listo = [];
    return temp_word

class nl_factory:

    def __init__(self, line_width, sys_new_line_character):

        self.char_count_line_max = line_width
        self.new_line_character = sys_new_line_character
        self.char_count_line = 0
        self.word_count = 0

    def word_handler(self, word: str):
        self.word_count += 1
        # The character count with a space and the new word
        char_count_line_with_word = self.char_count_line + 1 + len(word)
        add_dash = add_whitespace = add_line = False
        temp_word = ""
        char_count_extra = self.char_count_line_max - char_count_line_with_word

        # IF the line has the exact number of characters its supposed to have
        if char_count_line_with_word == self.char_count_line_max:
            self.char_count_line = 0
            temp_word = append_new_line(word, self.new_line_character)
        elif char_count_line_with_word < self.char_count_line_max:
            self.char_count_line += len(word) + 1
            temp_word = append_whitespace(word)
        elif len(word) == abs(char_count_extra):
            temp_word = append_new_line(temp_word, self.new_line_character) + word + ' '
            self.char_count_line = len(word) + 1
        elif char_count_line_with_word > self.char_count_line_max:
            self.char_count_line = abs(char_count_extra) + 1
            temp_word = append_newline_with_dash(word, char_count_extra, self.new_line_character)
        return temp_word


    def get_word_count(self):
        return self.word_count
