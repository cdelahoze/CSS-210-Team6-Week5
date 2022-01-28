import random




class word:


    def __init__(self):
        with open('testing/words.txt') as f:
            lines = f.readlines()

            temp_list = []
            for line in lines:
        
                temp_list.append((line.strip("\n")).upper())
        self.words_list = temp_list
        self.word = 0
        pass


    def blanks_letters(self, guessed_letters):
        pass


class TerminalService():
    """A service that handles terminal operations
    
    The responsibility of the TerminalService is to provide input and output operations for the terminal"""
    
    def __init__(self):
        pass



