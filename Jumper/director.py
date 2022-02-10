import random
from Jumper.game import Skydiver
from Jumper.support import word

MySkydiver = Skydiver()
MyWord = word()

class game:

    def __init__(self):

        spell_word = list(MyWord.word)
        length_word = len(spell_word)

        cartoons = MySkydiver.create_cartoon()
        underscores = MyWord.create_puzzle()
        sum = 0

        while MySkydiver.is_a_draw(cartoons):

            MyWord.display_underscore(underscores, length_word)
            MySkydiver.display_cartoon(cartoons)
            letter = input("Guess a leter [a-z]: ").upper()
            MyWord.make_move(underscores, spell_word, length_word, letter)
            MyWord.puzzle_mistake(spell_word, length_word, letter)
            result = MyWord.puzzle_mistake(spell_word, length_word, letter)
            sum += result
            puzzle = sum
            MySkydiver.make_move(cartoons, puzzle)
        
        MySkydiver.display_cartoon(cartoons)
        print("You have no more parachute the game is over!")
        print() 

      