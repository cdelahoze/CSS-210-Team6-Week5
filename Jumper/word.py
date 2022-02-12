import random

class list():

    def __init__(self):
     
        with open('words.txt') as f:
            lines = f.readlines()

            temp_list = []
            for line in lines:
        
                temp_list.append((line.strip("\n")).upper())
            
        self.__words_list = temp_list
        self.word = (random.choice(self.__words_list))
