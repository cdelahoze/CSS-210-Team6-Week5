import random
from Jumper.game import Skydiver
from Jumper.support import Word


MyWord = Word()

class game(Skydiver):

    def __init__(self):

        spell_word = list(MyWord.word)
        length_word = len(spell_word)

        cartoons = self.create_cartoon()
        underscores = MyWord.create_puzzle()
        sum = 0

        while self.is_a_draw(cartoons):

            MyWord.display_underscore(underscores, length_word)
            self.display_cartoon(cartoons)
            letter = input("Guess a leter [a-z]: ").upper()
            MyWord.make_move(underscores, spell_word, length_word, letter)
            MyWord.puzzle_mistake(spell_word, length_word, letter)
            result = MyWord.puzzle_mistake(spell_word, length_word, letter)
            sum += result
            puzzle = sum
            self.make_move(cartoons, puzzle)
        
        self.display_cartoon(cartoons)
        print("You have no more parachute the game is over!")
        print() 

      