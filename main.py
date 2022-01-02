"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name    : Ryan Finally
Date    : January 2nd, 2022
Place   : Pontianak, West Borneo, Indonesia

This is a simple program which will ask you to guess a number and 
give a hint for every wrong guesses that you made.

We start by defining the key concept of this program 
based on the description
-finish     : A condition when the game ended  
-ingame     : A condition when the player are given the rules
              and guessing the number chosen by the program
-start      : A condition when the program ask whether the player 
              wants to play or not
-intro      : A condition when the program welcome the player and
              ask his/her name

Let us get into the detail.
finish  : 
- victory message
- defeat message

ingame  :
- rules
- play

start   :
- proceed?

intro   :
- welcome message
- ask name

Each of this key concept will be made as class
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from sys import exit

class Finish:
    def victory_message(self, number, guess):
        self.number = number
        self.guess = guess
        print("That was awesome!!!\n")
        print(f"Your guess was {self.guess}.")
        print(f"The secret number was {self.number}.")
        exit()

    def defeat_message(self, number, guess):
        self.number = number
        self.guess = guess
        print("Too bad. You almost got it.\n")
        print(f"Your guess was {self.guess}.")
        print(f"The secret number was {self.number}.")
        print("\nTry again later!")
        exit()

class In_game:
    def rule():
        pass
    def play():
        pass

class Start:
    def proceed():
        pass

class Intro:
    def welcome_message():
        pass

    def username():
        pass


def main():
    pass

if __name__ == "__main__":
    main()



