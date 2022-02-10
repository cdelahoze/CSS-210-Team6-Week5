import random

class word:

    def __init__(self):
        with open('words.txt') as f:
            lines = f.readlines()

            temp_list = []
            for line in lines:
        
                temp_list.append((line.strip("\n")).upper())
            
        self.words_list = temp_list
        self.word = (random.choice(self.words_list))

        
    # Create the Puzzle
    def create_puzzle(self):
        underscore = ["_", "_", "_","_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        return underscore

    def display_underscore(self, underscore, length_word):
        
        i = 0
           
        for i in range(length_word):
            
            print(f"{underscore[i]}", end=" ")
    
    def is_a_draw(self, underscore, length_word):
        
        if underscore[length_word] != "_" :
            return False
        return True 

    def make_move(self, underscore, spell_word, length_word, letter):
        
                
        for j in range(length_word):
            if letter == spell_word[j]:
                underscore[j] = spell_word[j]

    def puzzle_mistake(self, spell_word, length_word, letter):
         
        for j in range(length_word):
            if letter == spell_word[j]:
                return 0
            else:
                return 1      




